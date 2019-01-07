#*******
#* Read input from STDIN
#* Use echo or print to output your result, use the /n constant at the end of each result line.
#* Use:
#*      local_print (variable ); 
#* to display simple variables in a dedicated area.
#* ***/
import sys

lines = "5\n.....\n.#...\nC#M.O\n.#...\n.....".split("\n")

grid = []
f = []
lines = lines[1:]
n = len(lines)
for i in range(n):
    s = []
    for k in range(n):
        if lines[i][k] == '#':
            s += [1]
        elif lines[i][k] == ".":
            s += [0]
        elif lines[i][k] == "M":
            s += [3]
            pos = [i, k]
        elif lines[i][k] == "C":
            s += [2]
            f.append( [i, k] )
        elif lines[i][k] == "O":
            s += [0]
            end = [i,k]
    grid.append(s)

print([n,end])
print(grid)
j = 0
np = [ pos[:] ]
nc = f[:]
while grid[end[0]][end[1]] == 0:
    nnc = []
    for p in nc: 
        [i,k] = p
        if grid[i][(k+1)%n] == 0:
            grid[i][(k+1)%n] = 3
            nnc.append( [i,(k+1)%n] )
        if grid[i][(n+k-1)%n] == 0:
            grid[i][(n+k-1)%n] = 3
            nnc.append( [i,(n+k-1)%n] )
        if grid[(i+1)%n][k] == 0:
            grid[(i+1)%n][k] = 3
            nnc.append( [(i+1)%n,k] )
        if grid[(n+i-1)%n][k] == 0:
            grid[(n+i-1)%n][k] = 3
            nnc.append( [(n+i-1)%n,k] )
    nc = nnc[:]
    nnp = []
    for p in np:
        [i,k] = p[:]
        if grid[i][(k+1)%n] == 0:
            grid[i][(k+1)%n] = 2
            nnp.append( [i,(k+1)%n] )
        if grid[i][(n+k-1)%n] == 0:
            grid[i][(n+k-1)%n] = 2
            nnp.append( [i,(n+k-1)%n] )
        if grid[(i+1)%n][k] == 0:
            grid[(i+1)%n][k] = 2
            nnp.append( [(i+1)%n,k] )
        if grid[(n+i-1)%n][k] == 0:
            grid[(n+i-1)%n][k] = 2
            nnp.append( [(n+i-1)%n,k] )
    np = nnp[:]
    print(grid)
    j += 1
    
if grid[end[0]][end[1]] == 3:
    print(0)
else:
    print(j)






