# Problem : https://www.codechef.com/SNCKQL17/problems/SAMESNAK

#!/usr/bin/python

# Get direction of sname (Only axis parallel)
def get_direction(head, tail):
    x = 0

    y = 1
    # 2,1   2, -2
    if head[x] > tail[x] and head[y] == tail[y]:
        direction = 'left'
    elif head[x] < tail[x] and head[y] == tail[y]:
        direction = 'right'
    elif head[y] < tail[y] and head[x] == tail[x]:
        direction = 'up'
    elif head[y] > tail[y] and head[x] == tail[x]:
        direction = 'down'
    else:
        raise IOError, 'Vertex not axis parallel'

    return direction

# Collect vertices between head and tail
def get_vertices(head, tail):
    vertices = []
    d = get_direction(head, tail)

    x = 0
    y = 1
    vertices = []
    if d == 'right':
        for i in range(head[x], tail[x] + 1):
            vertices.append((i, head[y]))

    elif d == 'left':
        for i  in range(head[x], tail[x] - 1, -1):
            vertices.append((i, head[y]))

    elif d == 'up':
        for i in range(head[y], tail[y] + 1):
            vertices.append((head[x], i))

    elif d == 'down':
        for i in range(head[y], tail[y] - 1, -1):
            vertices.append((head[x], i))

    else:
        raise IOError, 'Direction not axis parallel'

    return vertices


# find the next node in direction (right/left/up/down)
def neighbour(vertex, direction):
    # eg: vertex = (2, 1)
    x = 0
    y = 1
    if direction == 'right':
        return (vertex[x] + 1, vertex[y])
    elif direction == 'left':
        return (vertex[x] - 1, vertex[y])
    elif direction == 'up':
        return (vertex[x], vertex[y] + 1)
    elif direction == 'down':
        return (vertex[x], vertex[y] - 1)
    else:
        raise IOError, 'Direction not axis parallel'

opposite = {'right' : 'left', 'left' : 'right', 'up' : 'down', 'down': 'up'}

# Get edges for all the nodes between head and tail.
# Get edges in both forward and reverse direction
def get_edges(head, tail):
    x = 0
    y = 1
    edge = {}

    direction = get_direction(head, tail)

    # head to tail
    for vertex in get_vertices(head, tail):
        if vertex == tail:
            continue
        edge[vertex] = [neighbour(vertex, direction)]

    # tail to head
    for vertex in get_vertices(tail, head):
        # No edge for head and tail
        if vertex == head:
            break

        if vertex in edge.keys(): # Append if entry exists
            val = edge[vertex]
            val.append(neighbour(vertex, opposite[direction]))
            edge[vertex] = val
        else: # Add if new entry
            edge[vertex] = [neighbour(vertex, opposite[direction])]

    return edge

# Return (s1 U s2)
def union(e1, e2):
    #display_edges(e1)
    #display_edges(e2)
    if len(e1.keys()) < len(e2.keys()):
        src = e1
        dest = e2
    else:
        src = e2
        dest = e1

    #display_edges(src)
    #display_edges(dest)

    for key in src.keys():
        if key in dest.keys(): #(8,1) in
            val = src[key] #[(x,y), (x,y)]
            for item in val:
                if not item in dest[key]:
                    dest[key].append(item)
        else:
            dest[key] = src[key]

    return dest

# helper
def display_edges(e):
    print '[','*' * 10
    for key in e.keys():
        print '\t%s = %s' %(key, e[key])
    print '*' * 10, ']'

# if a vertex has > 2 edges, return false
def check_edges(e):
    for key in e.keys():
        if len(e[key]) > 2:
            return False

    return True

visited = {}

def print_visited(edges):
    for key in edges.keys():
        print 'visited[%s] = %s' %(key, visited[key])

# Search for all vertices of the snake and mark the visited
def search(edges, vertex):

    visited[vertex] = True

    for node in edges[vertex]:
        if visited[node] == False:
                search(edges, node)

# Return true if all the vertex of the snake is connected
# and all vertex have edges <= 2
def is_connected(edges, head):

    for key in edges.keys():
        visited[key] = False

    search(edges, head)

    connected = True
    for key in edges.keys():
        if not visited[key]:
            connected = False
            break

    if connected:
        return True
    else:
        return False

def same_snake(s1, s2):
    head1 = s1[0]
    tail1 = s1[1]

    head2 = s2[0]
    tail2 = s2[1]

    # Collected vertices and edges for snake sighting1
    vertices1 = get_vertices(head1, tail1)
    edges1 = get_edges(head1, tail1)
    #display_edges(edges1)

    # Collected vertices and edges for snake sighting2
    vertices2 = get_vertices(head2, tail2)
    edges2 = get_edges(head2, tail2)
    #display_edges(edges2)

    edges = union(edges1, edges2)
    #display_edges(edges)

    if check_edges(edges) and is_connected(edges, head1):
        print 'yes'
    else:
        print 'no'

def main():
    no = int(raw_input())

    snake = []
    for inp in range(no):
        x11, y11, x12, y12 = raw_input().split()
        x21, y21, x22, y22 = raw_input().split()

        s1 = [(int(x11), int(y11)), (int(x12), int(y12))]
        s2 = [(int(x21), int(y21)), (int(x22), int(y22))]
        snake.append([s1,s2])

    # input format
    # s1 = [(2, 1), (8, 1)]
    # s2 = [(11, 1), (7, 1)]
    # s3 = s1
    # s4 = [(11, 1), (9, 1)]
    # s5 = s1
    # s6 = [(3, 1), (3, -2)]
    # s7 = s1
    # s8 = [(2, 1), (2, -2)]

    for sightings in snake:
        same_snake(sightings[0], sightings[1])

if __name__ == '__main__':
    main()
