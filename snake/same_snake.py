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
def get_edges(head, tail):
    #head = s[0]
    #tail = s[1]
    x = 0
    y = 1
    edge = {}

    direction = get_direction(head, tail)
    print 'direction =', direction

    for vertex in get_vertices(head, tail):
        edge[vertex] = [neighbour(vertex, direction)]

    for vertex in get_vertices(tail, head):
        # No edge for head and tail
        if vertex == head or vertex == tail:
            continue
        val = edge[vertex]
        val.append(neighbour(vertex, opposite[direction]))
        edge[vertex] = val

    return edge

def next_vertex(vertex, direction):
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
        raise IOError, 'Invalid direction: %s' %direction


# Return (s1 U s2)
def union(e1, e2):
    print e1
    print e2

def display_edges(e):
    for key in e.keys():
        print '%s = %s' %(key, e[key])

def same_snake(s1, s2):
    head1 = s1[0]
    tail1 = s1[1]

    head2 = s2[0]
    tail2 = s2[1]

    print head1, tail1
    vertices1 = get_vertices(head1, tail1)
    print 'vertices =', vertices1
    edges1 = get_edges(head1, tail1)
    display_edges(edges1)

    print head2, tail2
    vertices2 = get_vertices(head2, tail2)
    print 'vertices =', vertices2
    edges2 = get_edges(head2, tail2)
    display_edges(edges2)


def main():
    # no = int(raw_input())
    # for inp in range(no):
    #     x1, y1, x2, y2 = raw_input().split()
    #     s1 = [[int(x1), int(y1)], [int(x2), int(y2)]]

    #     x1, y1, x2, y2 = raw_input().split()
    #     s2 = [[int(x1), int(y1)], [int(x2), int(y2)]]

    #     print s1
    #     print s2

    s1 = [(2, 1), (8, 1)]
    s2 = [(3, 1), (3, -2)]

    same_snake(s1, s2)


if __name__ == '__main__':
    main()
