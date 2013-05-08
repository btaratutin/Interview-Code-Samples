# -*- coding: utf-8 -*-
"""
Towers of Hanoi Problem (http://en.wikipedia.org/wiki/Tower_of_Hanoi)
Solved using recursion
9.20.10
"""

def SolveHanoi(n, src, aux, dest):
    
	# Base Case
    if (n == 1):
        return [src[0:-1], aux, dest.append(src.pop())] # move src --> dest

	# Reducing Case
    else:
        print "%s, %s, %s" % (src, aux, dest)
        SolveHanoi(n-1, src, dest, aux) #Move the top N - 1 disks from Src to Aux (using Dst as an intermediary peg)
        print "%s, %s, %s" % (src, aux, dest)
        SolveHanoi(1, src, aux, dest) # Move bottom disk to dest
        print "%s, %s, %s" % (src, aux, dest)
        SolveHanoi(n-1, aux, src, dest) #Move N - 1 disks from Aux to Dst (using Src as an intermediary peg)
    
    print "end: %s, %s, %s" % (src, aux, dest)

if __name__ == "__main__":
	towers = range(4)
	towers.reverse()

	print SolveHanoi(len(towers), towers, [], [])

    
