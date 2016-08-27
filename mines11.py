import mines2
from mines2 import *
import pygame
import sys
from pygame.locals import *
import numpy

pygame.init()

matrix_four = numpy.array([[0,1,0,0,1,1,0,0,0,0,0,0,0,0,0,0],
                           [1,0,1,0,1,1,1,0,0,0,0,0,0,0,0,0],
                           [0,1,0,1,0,1,1,1,0,0,0,0,0,0,0,0],
                           [1,1,0,0,0,1,0,0,1,1,0,0,0,0,0,0],
                           [1,1,1,0,1,0,1,0,1,1,1,0,0,0,0,0],
                           [0,1,1,1,0,1,0,1,0,1,1,1,0,0,0,0],
                           [0,0,0,0,1,1,0,0,0,1,0,0,1,1,0,0],
                           [0,0,0,0,1,1,1,0,1,0,1,0,1,1,1,0],
                           [0,0,0,0,0,1,1,1,0,1,0,1,0,1,1,1]])

column_index = []
#index_array = [0 for i in range(9)]
index_check = [0 for i in range(9)]
column_array = []
one_index = []
index_sol =9 
M_corner = 4
N_box =16
deter_mines_corner = [[-1 for i in range(M_corner)]for j in range(M_corner)]

inter_matrix = [[0 for i in range(16)]for j in range(9)]
make_array = [-1 for i in range (N_box)]
final = [-1 for i in range(index_sol)]

def mark_value(index_1,index_2):
    m_mines = index_1
    n_mines = index_2
    while m_mines <9:
        n_mines = index_2
        while n_mines <9:
            if mines[m_mines][n_mines]==0:
                if n_mines+1<9:
                    click(m_mines,n_mines+1,2)
                if n_mines-1>=0:
                    click(m_mines,n_mines-1,2)
                if m_mines+1 <9 and n_mines+1 <9:
                    click(m_mines+1,n_mines+1,2)
                if m_mines-1 >=0 and n_mines-1 >=0:
                    click(m_mines-1,n_mines-1,2)
                if m_mines+1 < 9 and n_mines-1 >=0:
                    click(m_mines+1,n_mines-1,2)
                if m_mines-1 >=0 and n_mines+1<9 :
                    click(m_mines-1,n_mines+1,2)
                if  m_mines-1>=0:
                    click(m_mines-1,n_mines,2)
                if m_mines+1<9:
                    click(m_mines+1,n_mines,2)
            n_mines+=1
        m_mines+=1

def run_game(index_1,index_2):
    m = 0
    n = 0
    index = 0
    index_fin = 0
    count = 0;
    mark_value(index_1,index_2)
    final = [-1 for i in range(index_sol)]    
    # To store 16 value and 9 values in a array
    m_mines = index_1
    n_mines = index_2
    while m < M_corner:
        n = 0
        n_mines = index_2
        while n < M_corner:
            deter_mines_corner[m][n] = mines[m_mines][n_mines]
            make_array[index] = deter_mines_corner[m][n]
            index+=1
            if n<3 and m<3:
                if deter_mines_corner[m][n]!=-1:
                    final[index_fin] = deter_mines_corner[m][n]
                    count = count+1
                index_fin+=1
            n_mines+=1
            n+=1
        m_mines+=1
        m+=1
    print count

    print final
    # to set value and form the matrix(corner)
    m_mines = index_1
    n_mines = index_2
    if count >4 and count < 9:
        for inter_i in range(9):
            for inter_j in range(16):
                inter_matrix[inter_i][inter_j]=matrix_four[inter_i][inter_j]
                
        count_zero = 0 # to count the number of information bits
        count_minus = 0 # to count the number of unknown values
        count_one = 0 # to count the number of mines found
        index = 0
        value = 0
        in_row = 0 # to get the value of row in the mines matrix
        in_col = 0 #to get the value of column in the mines matrix
        number_mines = 0
        index_matrix = 0
        fin_index  =0
        i = 0
        
        iterate = 0
        # prints values for matrices surrounded by 1 
        while iterate == 0:
            for i in range(9):
                print "iterate",iterate
                if i ==0:
                    iterate = 1
                print "printing i"
                print i
                print "final"
                print final
                print "make array"
                print make_array
                index_array = [0 for ind in range(9)]
                if final[i]!=-1 and final[i]!=0:
                    count_zero = 0
                    count_minus = 0
                    count_one = 0
                    index = 0
                    for  j in range(15):
                        if matrix_four[i][j] == 1:
                            if make_array[j] == 10:
                                inter_matrix[i][j]=0
                                count_one +=1
                            elif make_array[j]== -1:
                                print "i am in "
                                inter_matrix[i][j]= -1
                                count_minus +=1
                                index_array[index] = j
                                index+=1;
                            else:
                                inter_matrix[i][j]=0
                                count_zero+=1
                    print matrix_four[i]
                    print index_array
                    if count_minus == final[i] - count_one and count_minus > 0:
                        for k in range(count_minus):
                            value = index_array[k]
                            make_array[value] = 10;
                            in_row = value / 4
                            in_col = value % 4
                            click(in_row+m_mines,in_col+n_mines,1)
                            number_mines = number_mines+1
                            if in_col<3 and in_row<3 :
                                fin_index = in_row*3 + in_col
                                final[fin_index] = 10
                            iterate = 0
            
                    elif final[i] - count_one == 0 and count_minus>0:
                        for p in range(count_minus):
                            value = index_array[p]
                            in_row = value / 4
                            in_col = value % 4
                            click(in_row+m_mines,in_col+n_mines,2)
                            make_array[value] = mines[in_row+m_mines][in_col+n_mines]
                            if in_col < 3 and in_row <3:
                                fin_index = in_row*3 + in_col
                                final[fin_index] = make_array[value]
                            iterate = 0
                    elif count_minus != 0:
                        column_array.append(inter_matrix[i])
                        column_index.append(i)
                        one_index.append(count_minus)
                        index_matrix +=1
        
        # deterministic substitution method 
        m_mines = index_1
        n_mines = index_2
        stop_counter = 0
        print "hi"
        for i in range(9):
            if(final[i]==-1):
                stop_counter +=1
                
        if stop_counter>0:
            change = 0
            column_check = 0
            index = 0
            
            for i in range(index_matrix):
                j = i+1
                while j<index_matrix:
                    column_check = 0
                    index = 0
                    ind  = 0
                    change_value = 0
                    count_one = 0
                    if one_index[i] > one_index[j]:
                             change = one_index[i]
                             one_index[i] =one_index[j]
                             one_index[j]= change
                             change_value +=1
                    if one_index[i] < one_index[j]:
                        for k in range(16):
                             if column_array[j][k] == -1 and column_array[i][k] == -1:
                                 column_array [j][k] = 0
                                 column_check+=1
                             elif column_array[j][k]==-1 and column_array[i][k] != -1:
                                 index_check[index] = k
                                 index += 1
                             if column_array[j][k] == 1:
                                 count_one+=1
                                 
                        if column_check == one_index[i]:
                            ind = column_index[i]
                            if index == final[ind]-count_one and index >=0:
                                for p in range(index):
                                    value = index_check[p]
                                    in_row = value / 4
                                    in_col = value % 4
                                    click(in_row+m_mines,in_col+n_mines,2)
                                    if in_col < 3 and in_row<3:
                                        fin_index = in_row*3 + in_col
                                        final[fin_index] = make_array [value]

                            if change_value >0:
                             change = one_index[i]
                             one_index[i] =one_index[j]
                             one_index[j]= change        
                    j+=1

            
    #to save changes in mines
    m_mines = index_1
    n_mines = index_2
    index =0;
    while m_mines < index_1+4:
        n_mines = index_2
        while n_mines < index_2+4:
            mines[m_mines][n_mines] = make_array[index]
            index+=1
            n_mines+=1
        m_mines+=1

    # to print all values
    for i in range(4):
        for j in range(4):
            print '{:2}'.format(deter_mines_corner[i][j]),
        print
    print
    for i in range(9):
        for j in range(9):
            print '{:2}'.format(mines[i][j]),
        print
    print
    print make_array
    print "final value"
    print final
    pygame.display.update()
   # while True:
    #     for event in pygame.event.get([QUIT]):
     #       if event.type == QUIT:
      #          pygame.quit()
       #         sys.exit()
#run_game(0,0)

                

