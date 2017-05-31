#!/usr/bin/python

def gety(l):
    return l[1]

g = [[2, 4], [5, 6], [9, -1], [-2, 5], [5, -2]]

print sorted(g, key=gety)

