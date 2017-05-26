#!/usr/bin/python

import sys

def unique_center(inp):
    l = len(inp)
    if l >= 3 and (l % 2 != 0):
        return True
    else:
        return False

def start_and_end(inp):
    if inp[0] == 1 and inp[-1] == 1:
        return True
    else:
        return False

def check_order(inp):
    l = len(inp)
    if l % 2 == 0 or l < 2:
        return False

    center = l / 2

    # check left half
    for i in range(center):
        if inp[i + 1] == inp[i] + 1:
            continue
        else:
            return False

    # check reverse half
    for i in range(l - 1, center, -1):
        if inp[i] + 1 == inp[i - 1] :
            continue
        else:
            return False

    return True

def check_for_temple(length, heights):
    #print length
    #print heights
    h = heights.split()
    res = map(int, h)
    if unique_center(res) and start_and_end(res) and check_order(res):
        return True

def main():
    no = int(sys.stdin.readline())
    for i in range(no):
        length = int(sys.stdin.readline())
        heights = sys.stdin.readline()
        if check_for_temple(length, heights):
            print 'yes'
        else:
            print 'no'

if __name__ == '__main__':
    main()
