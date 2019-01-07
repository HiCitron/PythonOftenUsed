# -*- coding: utf-8 -*-

# [[1, 2], [1, 3], [2, 1], [2, 3], [3, 1], [3, 2]]
def allPerm( l, n, s = [] ):
    if n == 0:
        return [s]
    else:
        perm = []
        for i in range(len(l)):
            perm += allPerm( l[:i] + l[i+1:], n-1, s + [l[i]] )
        return perm

# [[1, 1], [1, 2], [1, 3], [2, 1], [2, 2], [2, 3], [3, 1], [3, 2], [3, 3]]
def allGen( l, n, s = [] ):
    if n == 0:
        return [s]
    else:
        gen = []
        for i in range(len(l)):
            gen += allGen( l, n-1, s + [l[i]] )
        return gen

# [[1, 2], [1, 3], [2, 3]]
def allSets( l, n, s = [] ):
    if n == 0:
        return [s]
    else:
        sub = []
        for i in range(len(l)):
            sub += allSets( l[i+1:], n-1, s + [l[i]] )
        return sub

# [[1, 1], [1, 2], [1, 3], [2, 2], [2, 3], [3, 3]]
def allSetsR( l, n, s = [] ):
    if n == 0:
        return [s]
    else:
        sub = []
        for i in range(len(l)):
            sub += allSetsR( l[i:], n-1, s + [l[i]])
        return sub
