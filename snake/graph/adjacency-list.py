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


class Graph():
    def __init__(self):
        self.graph = []

    def display(self):
        print '*' * 10
        for i in range(len(self.graph)):
            print i + 1, '=' , self.graph[i]
        print '*' * 10

    def is_empty(self):
        if self.graph == []:
            return True

    def append(self, item):
        self.graph.append(item - 1)

    def insert(self, index, item):
        self.graph.insert(index, item)

    def modify(self, index, value):
        self.graph[index] = value

    def getIndex(self, index):
        return self.graph[index - 1]

def main():
    nodes = 4
    edges = 5

    g = Graph()
    # g.display()
    # g.append([1,2,3])
    # g.append([2,3,4])
    # g.insert(1, [0,0,0])
    # g.modify(1, [1,1,1])
    g.insert(1, [2])
    g.insert(2, [4])
    g.insert(3, [1,4])
    g.insert(4, [2])

    g.display()

if __name__  == '__main__':
    main()
