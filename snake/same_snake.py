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
        direction = 'error'

    return direction

# Get edges of all vertices
def get_edges(s):
    head = s[0]
    tail = s[1]
    x = 0
    y = 1
    edge = []

    direction = get_direction(head, tail)
    if direction == 'right':
        for i in range(head[x], tail[x] + 1):
            edge.append([i, head[y]])

    elif direction == 'left':
        for i  in range(head[x], tail[x] - 1, -1):
            edge.append([i, head[y]])

    elif direction == 'up':
        for i in range(head[y], tail[y] + 1):
            edge.append([head[x], i])

    elif direction == 'down':
        for i in range(head[y], tail[y] - 1, -1):
            edge.append([head[x], i])

    else:
        edge = -1

    return edge

# Return (s1 U s2)
def union(s1, s2):
    s = s1 + s2
    return s

def same_snake(s1, s2):
    e1 = get_edges(s1)
    print 'e1 = ', e1
    e2 = get_edges(s2)
    print 'e2 = ', e2
    print union(e1, e2)

def main():
    # no = int(raw_input())
    # for inp in range(no):
    #     x1, y1, x2, y2 = raw_input().split()
    #     s1 = [[int(x1), int(y1)], [int(x2), int(y2)]]

    #     x1, y1, x2, y2 = raw_input().split()
    #     s2 = [[int(x1), int(y1)], [int(x2), int(y2)]]

    #     print s1
    #     print s2

    s1 = [[2, 1], [8, 1]]
    s2 = [[3, 1], [3, -2]]

    same_snake(s1, s2)
if __name__ == '__main__':
    main()
