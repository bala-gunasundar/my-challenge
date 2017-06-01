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

def get_edges(head, tail):
    #head = s[0]
    #tail = s[1]
    x = 0
    y = 1
    edge = {}

    direction = get_direction(head, tail)
    print direction
    for vertex in get_vertices(head, tail):
        edge[vertex] = neighbour(vertex, direction)

    # Last one doesn't have an edge
    del edge[tail]

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
def union(s1, s2):
    s = set(s1) | set(s2)
    return s

def same_snake(s1, s2):
    head1 = s1[0]
    tail1 = s1[1]

    head2 = s2[0]
    tail2 = s2[1]

    print head1, tail1
    print get_vertices(head1, tail1)
    print get_edges(head1, tail1)

    print '*' * 10
    print head2, tail2
    print get_vertices(head2, tail2)
    print get_edges(head2, tail2)


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
    s2 = [(11, 1), (7, 1)]

    s3 = [(2,1), (8,1)]
    s4 = [(3,1), (3,8)]
    same_snake(s3, s4)


if __name__ == '__main__':
    main()
