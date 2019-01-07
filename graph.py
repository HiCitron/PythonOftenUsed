# -*- coding: utf-8 -*-

# links = [ [ [2, 3], [], [0, 3] ] ]
#           point 0 linked to 2 with a distance of 3
def Pathfind( s, links ):
    n = len(links)
    A = [ [float('inf'),-1] for i in range(n) ]
    unv = [1]*n
    reach = [float('inf')] * n
    A[s][0], unv[s], reach[s], mini = 0,0,0,0
    while mini != float('inf'):
        nextP = reach.index( mini )
        reach[nextP] = float('inf')
        unv[nextP] = 0
        for i in range( len( links[nextP] ) ):
            if unv[ links[nextP][i][0] ] == 1:
                k = links[nextP][i]
                if A[ k[0] ][0] > A[ nextP ][0] + k[1]:
                    A[ k[0] ] = [ A[ nextP ][0] + k[1], nextP ]
                    reach[ k[0] ] = A[ nextP ][0] + k[1]
        mini = min(reach)
    return A

# links = [ [2], [], [0] ]
#       point 2 and 0 linked, distance always = 1
def PathfindUnitary( s, links ):
    n = len(links)
    A = [ [float('inf'),-1] for i in range(n) ]
    unv = [1]*n
    reach = [float('inf')] * n
    A[s][0], unv[s], reach[s], mini = 0,0,0,0
    while mini != float('inf'):
        nextP = reach.index( mini )
        reach[nextP] = float('inf')
        unv[nextP] = 0
        for i in range( len( links[nextP] ) ):
            if unv[ links[nextP][i] ] == 1:
                k = links[nextP][i]
                if A[ k ][0] > A[ nextP ][0] + 1:
                    A[ k ] = [ A[ nextP ][0] + 1, nextP ]
                    reach[ k ] = A[ nextP ][0] + 1
        mini = min(reach)
    return A

# grid = [ [0,0,0,1,0], [0,1,1,1,0], [0,0,0,0,0], [1,1,0,1,0], [1,0,0,0,0] ]
def PathfindGrid( pos, grid ):
    n,m = len(grid[0]), len(grid)
    A = [ [ float('inf'), -1 ] for i in range(n*m) ]
    reach = [ float('inf') for i in range(n*m) ]
    unv = [1]*(n*m)
    s = pos[1]*n + pos[0]
    A[s][0] , reach[s], unv[s], mini = 0, 0, 0, 0
    while mini != float('inf'):
        nP = reach.index( mini )
        P = [ nP % n, int(nP/n) ]
        reach[nP] = float('inf')
        unv[nP] = 0
        if P[0] - 1 >= 0:
            if grid[P[1]][P[0]-1] == 0 and unv[nP-1]:
                if A[nP][0] + 1 < A[nP-1][0]:
                     A[nP-1] = [ A[nP][0] + 1, nP ]
                     reach[nP-1] = A[nP][0] + 1
        if P[0] + 1 <= n-1:
            if grid[P[1]][P[0]+1] == 0 and unv[nP+1]:
                if A[nP][0] + 1 < A[nP+1][0]:
                     A[nP+1] = [ A[nP][0] + 1, nP ]
                     reach[nP+1] = A[nP][0] + 1
        if P[1] - 1 >= 0:
            if grid[P[1]-1][P[0]] == 0 and unv[nP-n]:
                if A[nP][0] + 1 < A[nP-n][0]:
                     A[nP-n] = [ A[nP][0] + 1, nP ]
                     reach[nP-n] = A[nP][0] + 1
        if P[1] + 1 <= m-1:
            if grid[P[1]+1][P[0]] == 0 and unv[nP+n]:
                if A[nP][0] + 1 < A[nP+n][0]:
                     A[nP+n] = [ A[nP][0] + 1, nP ]
                     reach[nP+n] = A[nP][0] + 1
        mini = min(reach)
    return A

# links with values
def MST( links ):
    n = len(links)
    unv = [0] + [1]*(n-1)
    best = [[float('inf'), -1] for i in range(n) ]
    nlinks = [ [] for i in range(n) ]
    mini, nextP = [0, -1], 0
    while mini[0] != float('inf'):
        for i in range( len(links[nextP]) ):
            if unv[ links[nextP][i][0] ] == 1:
                k = links[nextP][i]
                if k[1] < best[ k[0] ][0]:
                    best[ k[0] ] = [ k[1], nextP ]
        mini = min(best)
        print(best)
        if mini[0] != float('inf'):
            nextP = best.index( mini )
            nlinks[ mini[1] ].append( [ nextP, mini[0] ] )
            nlinks[ nextP ].append( [ mini[1], mini[0] ] )
            best[ nextP ] = [float('inf'), -1]
            unv[ nextP ] = 0
    return nlinks

# complete graph with Distance function    
def MSTComplete( s, points ):
    return s

s = 0
links = [ [[1,5],[2,2]], [[0,5],[2,3],[3,1]], [[0,2],[1,3],[3,1],[4,5]], [[1,1],[2,1],[4,3]], [[2,5],[3,3]] ]
print( Pathfind( 0, links ) )
