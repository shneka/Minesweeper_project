import mines2
from mines2 import *
import pygame
import sys
from pygame.locals import *
import numpy
from mines12 import *
from mines13 import *
from mines14 import *

value = 4
def number_mines(x,y):
    count = 0
    index_x = x+3
    index_y = y+3
    print x,y
    x_val = x
    y_val = y 
    while x_val<index_x:
        y_val = y
        while y_val<index_y:
            print mines[x_val][y_val]
            if mines[x_val][y_val]!=-1:
                count +=1
            y_val+=1
        x_val+=1
    return count
def call_game():
    set_game()
    click(0,0,2)
    mark_value(0,0)
    value_1 = [0 for i_1 in range(6)] 
    for index_1 in range(6):
        value_1[index_1]=number_mines(0,index_1)
        if value_1[index_1]>4 and value_1[index_1]<9:
            run_game(0,index_1)
            print mines
    run_game_three(0,6)

    value_2 = [0 for i_2 in range(7)]
    for index_2 in range(6):
        value_2[index_2]=number_mines(index_2,0)
        if value_2[index_2]>4 and value_2[index_2]<9:
            run_game(index_2,0)
            print mines     
    run_game_three(6,0)
   
    value_3 = [0 for i_3 in range(6)]
    for index_3 in range(6):
        print "doing loop 3"
        print index_3
        value_3[index_3]=number_mines(5,index_3)
        if value_3[index_3]>4 and value_3[index_3]<9:
            run_game(5,index_3)
            print mines
    run_game_three(6,5)

    value_5 = [0 for i_3 in range(6)]
    for index_5 in range(6):
        print "doing loop 5"
        print index_5
        value_5[index_3]=number_mines(index_3,6)
        if value_3[index_5]>4 and value_5[index_5]<9:
            run_game_three(index_3,6)
            print mines
            
    value_4 = [0 for i_3 in range(3)]
    for index_4 in range(3):
        print "doing loop 4"
        print index_4
        value_4[index_4]=number_mines(2,index_4)
        if value_4[index_4]>4 and value_4[index_4]<9:
            run_game_five(2,index_4)
            print mines
    # to make the program quit on close button
    while True:
         for event in pygame.event.get([QUIT]):
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
call_game()
