#!/usr/bin/python

import sys

def checkInput(s):

    start = 'H'
    end = 'T'

    #print s
    for ch in s:
        # search need_ch, if end print invalid
        # if start found, swap start and end
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
    f = open('snake.txt', 'r')
    no = int(f.readline())
    for i in range(no):
        strlen = f.readline()
        input = f.readline()
        if checkInput(input):
            print 'Valid'
        else:
            print 'Invalid'

if __name__ == '__main__':
    main()
