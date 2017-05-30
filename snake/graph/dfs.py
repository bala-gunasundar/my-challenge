# Depth first search sample code

#!/usr/bin/python
from adjacency_list import Graph

def main():
    #init graph with nodes and edges
    g = Graph(6, 4)

    # create edges
    g.modify(1, [2, 3])
    g.modify(2, [3])
    g.modify(3, [2])
    g.modify(4, [5])

    # Display the edges
    g.display()

    # Find the connected component
    print 'No of connected components = %d' %g.count_connected()

if __name__ == '__main__':
    main()
