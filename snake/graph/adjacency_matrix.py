#
# https://www.hackerearth.com/practice/notes/graph-theory-part-i/
#
# Directed graph
#
#  1 -------> 2 --
#  |          ^   |
#  |          |   |
#  |          |   |
#  v          |   |
#  3 -------> 4 <-
#

#!/usr/bin/python


def print_matrix(m, n):
    for i in range(n):
        print m[i]

def store_edge(m, x, y):
    x -= 1
    y -= 1
    m[x][y] = 1

def get_edge(m, x, y):
    x -= 1
    y -= 1

    if m[x][y] == 1:
        return True
    else:
        return False

def main():

    # matrix height and width
    nodes = 4
    edges = 5

    # Create matrix
    matrix = [[0 for x in range(nodes)] for y in range(nodes)]

    store_edge(matrix, 1, 2)
    store_edge(matrix, 2, 4)
    store_edge(matrix, 3, 1)
    store_edge(matrix, 3, 4)
    store_edge(matrix, 4, 2)

    print_matrix(matrix, nodes)

    if get_edge(matrix, x=2, y=1):
        print 'yes'
    else:
        print 'no'

if __name__  == '__main__':
    main()
