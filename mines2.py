#To set the working board and to make necessary changes when the values are passed
# The program is also used to refresh and start a new game

import pygame
import sys
from pygame.locals import * 
import minesweeper2
from minesweeper2 import minesweeper_grid  
import time

pygame.init()

N=10;
#mines = [[-1 for i in range(N-1)]for i in range (N-1)]

#defing the display

size = ((N-1)*50)+(N*5);
setDisplay = pygame.display.set_mode((size,size))
pygame.display.set_caption("MineSweeper")

# defining colours to be used
white = (255,255,255)
black = (0,0,0)
grey = (125,125,125)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
yellow =  (255,255,0)

i= 0;
row = 50;
column= 50;
margin = 5;
mines = [[-1 for i in range(N-1)]for i in range (N-1)]

def whatNext():
    for event in pygame.event.get([KEYDOWN,KEYUP,QUIT]):
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            continue
        return event.key
    return None

def msgSurface():
    
    for i in range(N):
        row_pos = minesweeper_grid.mine_row[i];
        column_pos = minesweeper_grid.mine_column[i]
        row_len = ((row_pos*row)+((row_pos+1)*margin))+25
        column_len = ((column_pos*column)+((column_pos+1)*margin))+25
        pygame.draw.circle(setDisplay,red,(column_len,row_len),15,0)
        
    font_small = pygame.font.Font("freesansbold.ttf",20)
    font_large = pygame.font.Font("freesansbold.ttf",75)

    text_small = font_small.render("Press any key to continue",True,blue)
    text_large = font_large.render("YOU DIED",True,red)

    titleTextRect = (45, int (size/2)-50)
    typTextRect =(int (size/2)-120,int (size/2)+120)
    setDisplay.blit(text_small,typTextRect)
    setDisplay.blit(text_large, titleTextRect)
    
    while whatNext()== None:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
        pygame.display.update()

    set_game()

               
   

def set_game():
    number = 0
    minesweeper2.minesweeper_grid()
    setDisplay.fill(black)
    #mines = [[-1 for i in range(N-1)]for i in range (N-1)]
    for i in range(N):
        row_len = (i*row)+((i+1)*margin)
        for j in range(N):
            column_len = (j*column)+((j+1)*margin)
            pygame.draw.rect(setDisplay,yellow,(row_len,column_len,50,50))
    
def click(row_pos,column_pos, mouse_control):
    row_len = ((row_pos*row)+((row_pos+1)*margin))+10
    column_len = ((column_pos*column)+((column_pos+1)*margin))+10

    if(mouse_control== 1):
        if(mines[row_pos][column_pos]==-1):
            pygame.draw.rect(setDisplay,red,(column_len,row_len,15,15))
            pygame.draw.lines(setDisplay,red,False,[(column_len,row_len+15),(column_len,row_len+25)],2)
            mines[row_pos][column_pos] = 10;

        elif(mines[row_pos][column_pos]==10):
            pygame.draw.rect(setDisplay,yellow,(column_len,row_len,15,15))
            pygame.draw.lines(setDisplay,yellow,False,[(column_len,row_len+15),(column_len,row_len+25)],2)
            mines[row_pos][column_pos] = -1;

    elif(mines[row_pos][column_pos]==-1):
        message = minesweeper2.minesweeper_grid.matrix[row_pos][column_pos]
        if (message!=10):
            if(message == 0):
                i = row_pos
                while(i<N-1):
                    j = column_pos
                    row_len = ((i*row)+((i+1)*margin))
                    if(minesweeper_grid.matrix[i][j]==0):
                        while(j<N-1):
                            column_len = ((j*column)+((j+1)*margin))
                            if(minesweeper_grid.matrix[i][j]==0):
                                pygame.draw.rect(setDisplay,grey,(column_len,row_len,50,50))
                                mines[i][j]=0
                            else:
                                message = minesweeper_grid.matrix[i][j];
                                font = pygame.font.SysFont(None, 48)
                                text = font.render(str(message),True,red)
                                setDisplay.blit(text,(column_len+10,row_len+10))
                                mines[i][j] = message
                                break
                            j+=1

                        j = column_pos
                        while(j>=0):
                            column_len = ((j*column)+((j+1)*margin))
                            if(minesweeper_grid.matrix[i][j]==0):
                                pygame.draw.rect(setDisplay,grey,(column_len,row_len,50,50))
                                mines[i][j]=0

                            else:
                                message = minesweeper_grid.matrix[i][j];
                                font = pygame.font.SysFont(None, 48)
                                text = font.render(str(message),True,red)
                                setDisplay.blit(text,(column_len+10,row_len+10))
                                mines[i][j] = message;
                                break
                            j-=1
                    else:
                        j = column_pos
                        column_len = ((j*column)+((j+1)*margin))
                        message = minesweeper_grid.matrix[i][j];
                        font = pygame.font.SysFont(None, 48)
                        text = font.render(str(message),True,red)
                        setDisplay.blit(text,(column_len+10,row_len+10))
                        mines[i][j] = message;
                        break
                    i+=1
                i = row_pos


                while(i>=0):
                    j = column_pos
                    row_len = ((i*row)+((i+1)*margin))
                    if(minesweeper_grid.matrix[i][j]==0):
                        while(j<N-1):
                            column_len = ((j*column)+((j+1)*margin))
                            if(minesweeper_grid.matrix[i][j]==0):
                                pygame.draw.rect(setDisplay,grey,(column_len,row_len,50,50))
                                mines[i][j]=0

                            else:
                                message = minesweeper_grid.matrix[i][j];
                                font = pygame.font.SysFont(None, 48)
                                text = font.render(str(message),True,red)
                                setDisplay.blit(text,(column_len+10,row_len+10))
                                mines[i][j] = message;
                                break
                            j+=1

                        j = column_pos
                        while(j>=0):
                            column_len = ((j*column)+((j+1)*margin))
                            if(minesweeper_grid.matrix[i][j]==0):
                                pygame.draw.rect(setDisplay,grey,(column_len,row_len,50,50))
                                mines[i][j]=0

                            else:
                                message = minesweeper_grid.matrix[i][j];
                                font = pygame.font.SysFont(None, 48)
                                text = font.render(str(message),True,red)
                                setDisplay.blit(text,(column_len+10,row_len+10))
                                mines[i][j] = message;
                                break
                            j-=1
                    else:
                        j = column_pos
                        column_len = ((j*column)+((j+1)*margin))
                        message = minesweeper_grid.matrix[i][j]
                        font = pygame.font.SysFont(None, 48)
                        text = font.render(str(message),True,red)
                        setDisplay.blit(text,(column_len+10,row_len+10))
                        mines[i][j] = message;
                        break
                    i-=1
                print(mines)


            else:
                font = pygame.font.SysFont(None, 48)
                text = font.render(str(message),True,red)
                setDisplay.blit(text,(column_len,row_len))
                mines[row_pos][column_pos] = message;

        else:
            msgSurface()
    
    pygame.display.update()

