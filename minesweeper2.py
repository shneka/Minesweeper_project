import sys
import random

#number of squares in the grid
N = 9
#number of mines 
M = 10
# To initialise the values in the matrix to 0

def minesweeper_grid():
    minesweeper_grid.matrix = [[0 for i in range(N)]for i in range(N)]
    r =[0 for i in range(M)]
    var = [-1 for i in range(M)]
    minesweeper_grid.mine_row = [-1 for i in range(M)]
    minesweeper_grid.mine_column = [-1 for i in range(M)]
    
    for k in range(M):
        r[k] = random.randint(1,81)
        while r[k] in var:
            r[k] = random.randint(1,81)
        var[k]=r[k]
        q = r[k]/N
        rem = r[k]%N
        if (rem ==0 and q !=0):
            minesweeper_grid.matrix[q-1][N-1]=10
            minesweeper_grid.mine_row[k]=q-1
            minesweeper_grid.mine_column[k]=N-1
        else:
            minesweeper_grid.matrix[q][rem-1] = 10
            minesweeper_grid.mine_row[k]=q
            minesweeper_grid.mine_column[k]=rem-1

    #print(r)
    #print(minesweeper_grid.mine_row,minesweeper_grid.mine_column)

    for k in range(M):
        q = r[k]/N
        rem = r[k]%N
        if(rem==0 and q!=0):
            q=q-1
            rem = N
        for i in range(q-1,q+2):
            for j in range(rem-2,rem+1):
                if not(i == q and j == rem-1):
                    if(i<N and i>=0 and j>=0 and j<N): 
                        if(minesweeper_grid.matrix[i][j]!=10):
                            minesweeper_grid.matrix[i][j]+=1
    
    for i in range(N):
        for j in range(N):
            print '{:2}'.format(minesweeper_grid.matrix[i][j]),
        print

