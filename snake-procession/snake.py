#!/usr/bin/python

import sys

def checkInput(s, strlen):

    start = 'H'
    end = 'T'

    for ch in s[:strlen]:
        if ch == start:
            start, end = end, start
        elif ch == end:
            return False
        else:
            continue

    if start == 'H' and end == 'T':
        return True
    else:
        return False

def main():
    no = int(sys.stdin.readline())
    for i in range(no):
        strlen = int(sys.stdin.readline())
        inp = sys.stdin.readline()
        if checkInput(inp, strlen):
            print 'Valid'
        else:
            print 'Invalid'

if __name__ == '__main__':
    main()
