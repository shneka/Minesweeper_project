#This program uses the deterministic algorithm and calls the previous program
#To implement deterministic algorithm
# 2 represents left click ad 1 represents right click

import mines2
from mines2 import *
import pygame
import sys
from pygame.locals import *
import numpy

pygame.init()
matrix_four = numpy.array([[0,1,0,1,1,0,0,0,0],
               [1,0,1,1,1,1,0,0,0],
               [0,1,0,0,1,1,0,0,0],
               [0,0,1,0,0,1,0,0,0],
               [1,1,0,0,1,0,1,1,0],
               [1,1,1,1,0,1,1,1,1],
               [0,1,1,0,1,0,0,1,1],
               [0,0,1,0,0,1,0,0,1],
               [0,0,0,1,1,0,0,1,0],
               [0,0,0,1,1,1,1,0,1],
               [0,0,0,0,1,1,0,1,0],
               [0,0,0,0,0,1,0,0,1],
               [0,0,0,0,0,0,1,1,0],
               [0,0,0,0,0,0,1,1,1],
               [0,0,0,0,0,0,0,1,1],
               [0,0,0,0,0,0,0,0,1]])

N = 9
M_corner = 4
M = 5
N_box =16
index_array = []
column_array = []
make_array = [-1 for i in range (N_box)]
final_solution = [-1 for i in range(N)]
deter_mines_corner = [[-1 for i in range(M_corner)]for j in range(M_corner)]
array_output = [[-2 for i in range(16)]for j in range(9)]

#performs Gaussian Elimination
def gauss_eliminate(index,column_array,array_output):
    for i in range(index):
        for k in range(index):
            array_output[i][k]=column_array[i][k]
    for i in range(index):
        p=0
        for j in range(index):
            if column_array[j][i]==1 and p==0:
                for k in range(index):
                    array_output[i][k]=column_array[j][k]
                    column_array[j][k]=-1
                p=1;
            elif column_array[j][i]==1 and p!=0:
                for l in range(index):
                    column_array[j][l]=(column_array[j][l]+array_output[i][l])%2
                    
    for i in range(index):
        j=i+1
        while j<=index:
            if array_output[i][j]==1:
                for k in range(index):
                    array_output[i][k]=(array_output[i][k]+array_output[j][k])%2
            j+=1
    count = 0
    for i in range(index):
        for j in range(index):
            if i==j and array_output[i][j]==1:
                count = count +1;
    if  count== index:
        print "Deterministic Solution"
    else:
        print "Reinforcement Learning"
# To start running the game
def run_game():
    set_game()
    click(0,0,2)
    inter_solution = [-1 for i in range (N_box)]
    m = 0
    n = 0
    index = 0
    count = 0
    index_final = 0
    while m < M_corner:
        n = 0
        while n < M_corner:
            deter_mines_corner[m][n] = mines[m][n]
            make_array[index] = deter_mines_corner[m][n]
            if n !=0:
                if deter_mines_corner[m][n-1]==0 or deter_mines_corner[m-1][n-1]==0:
                    click(m,n,2)
                    deter_mines_corner[m][n]=mines[m][n]
                    make_array[index] = deter_mines_corner[m][n]
            if  m<3 and n<3:
                if deter_mines_corner[m][n]!=-1:
                    count = count+1;
                    final_solution[index_final] = deter_mines_corner[m][n]
                index_final +=1;
            index+=1
            n+=1
        m+=1

    index_count =0
    count_values =0
    
    for i in range(4):
        for j in range(4):
            if i<3 and j<3:
                if (deter_mines_corner[i][j]!=-1):
                    index_array.append(index_count);
                    column_array.append(matrix_four[:,count_values]);
                    count_values = count_values+1;
                index_count+=1;
    if(count_values>4 and count_values < 9):
        gauss_eliminate(count_values,column_array,array_output)
    else:
        print("The output cannot be found")
    print "printing index"
    print index_array
    print "printing row"
    print column_array
    
    for i in range(9):
        for j in range(16):
            print '{:2}'.format(array_output[i][j]),
        print
    for i in range(M_corner):
        for j in range(M_corner):
            print '{:2}'.format(deter_mines_corner[i][j]),
        print
        
    for i in range(N):
        for j in range(N):
            print '{:2}'.format(mines[i][j]),
        print
    print matrix_four
    # To be able to quit and come out of the window
    
    while True:
         for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
run_game()
 
