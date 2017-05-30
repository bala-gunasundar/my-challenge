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
    nodes = 0
    edges = 0
    visited = []
    graph = []
    total_connected = 0

    def __init__(self, nodes, edges):
        self.graph = [[]] * nodes
        self.nodes = nodes
        self.edges = edges
        self.visited = [False] * nodes
        print self.visited

    def size(self):
        return len(self.graph)

    def display(self):
        print '*' * 10
        for i in range(len(self.graph)):
            print i + 1, '=' , self.graph[i]
        print '*' * 10

    def is_empty(self):
        if self.graph == []:
            return True

    def append(self, item):
        self.graph.append(item)

    def insert(self, index, item):
        self.graph.insert(index - 1, item)

    def modify(self, index, value):
        if type(value) is not list:
            raise ValueError, "Check argument 2 is a list"
        self.graph[index - 1] = value

    def getIndex(self, index):
        return self.graph[index - 1]

    # Depth first search
    def dfs(self, i):
        if i == 0:
            return

        print 'dfs', i
        self.visited[i] = True
        l = self.getIndex(i)
        for val in l:
            #print 'visited[%d] = %s' %(val, self.visited[val])
            if self.visited[val] == False:
                self.dfs(val)

    def count_connected(self):
        for i in range(self.nodes):
            if self.visited[i] == False:
                self.dfs(i)
                self.total_connected += 1

        return self.total_connected

def main():

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
