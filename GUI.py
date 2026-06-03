from gamelogic import Kakuro
import math
import sys
import random
sys.setrecursionlimit(5000)

import pygame
pygame.init()
fontsize = 25
font = pygame.font.Font(None, fontsize)
color = (255, 0, 255)
colorpressed = (248,212,7)
GRIDSIZE = 75
BORDER = 10 #maximal GRIDSIZE/2
def createKakuro(kakuro):
    global WIDTH 
    WIDTH = kakuro.x*GRIDSIZE
    global HEIGHT 
    HEIGHT = kakuro.y*GRIDSIZE

clicked = ()  
def mouse(k):
    global clicked
    if pygame.mouse.get_pressed()[0]==True:
        x,y = pygame.mouse.get_pos()
        if x<WIDTH and y<HEIGHT:
            x,y = math.floor(x/GRIDSIZE), math.floor(y/GRIDSIZE)
            if k.contenty[x][y] == 0 and k.contentx[x][y] == 0:
                clicked = (x,y)  

def keypressed(k):
    if event.type == pygame.KEYDOWN:
        if pygame.K_1 <= event.key <= pygame.K_9:
            if clicked != None:
                k.answers[clicked[0]][clicked[1]] = event.unicode
        elif pygame.K_s == event.key:
            wipeanswers(k)
            k.recursiveshell()
            print(k.recursiveshell())
        elif pygame.K_c == event.key:
            b = 0   
            for x in range(len(k.answers)):
                for y in range(len(k.answers[0])):
                    if k.answers[x][y]!=0:
                        if k.legal(x,y)==False:
                            b = 1
                            print(f"Stelle ({x}|{y}) ist illegal")
            if b == 0:
                print("puzzle is legal")
        elif pygame.K_SPACE == event.key:
            k.answers[clicked[0]][clicked[1]] = 0 
        elif pygame.K_r == event.key:
            wipeanswers(k)
            k.bfill()
            k.generator(random.randint(10000000,99999999))
            #k.constraintcreator()
            k.randomfill()
            k.sumup()
            wipeanswers(k) 
        elif pygame.K_w == event.key:
            wipeanswers(k)     
def wipeanswers(k):
    for x in range(len(k.answers)):
        for y in range(len(k.answers[0])):
            k.answers[x][y]=0
def drawgrid():
    
    for x in range(0, WIDTH, GRIDSIZE):
        for y in range(0, HEIGHT, GRIDSIZE):
            rect = pygame.Rect(x, y, GRIDSIZE, GRIDSIZE)
            if clicked == (round(x/GRIDSIZE),round(y/GRIDSIZE)):
                
                pygame.draw.rect(screen, colorpressed, rect, 1)
            else:
                pygame.draw.rect(screen, color, rect, 1)
            

def drawvalue(kakuro):
    for x in range(len(kakuro.contentx)):
        for y in range(len(kakuro.contentx[0])):
            xcon = kakuro.contentx[x][y]
            ycon = kakuro.contenty[x][y]
            if (xcon!=0 and xcon!="B" ):
                text = font.render(f"{xcon}", True, color)                                                                   #vllt muss x,y // GRIDSIZE
                screen.blit(text,(x*GRIDSIZE + GRIDSIZE*0.75, y*GRIDSIZE + GRIDSIZE*0.325))
            if (ycon!=0 and ycon!="B"):
                text = font.render(f"{ycon}", True, color)                                                                   #vllt muss x,y // GRIDSIZE
                screen.blit(text,(x*GRIDSIZE + GRIDSIZE*0.375, y*GRIDSIZE + GRIDSIZE*0.75))
            elif(xcon == 0 and ycon == 0):
                rect = pygame.Rect( x*GRIDSIZE + BORDER, y*GRIDSIZE + BORDER, GRIDSIZE - 2*BORDER, GRIDSIZE - 2*BORDER)
                pygame.draw.rect(screen, color, rect)
                if k.answers[x][y]!=0:
                    text = font.render(f"{k.answers[x][y]}", True, (0,0,0))                                                                   #vllt muss x,y // GRIDSIZE
                    screen.blit(text,(x*GRIDSIZE + GRIDSIZE*0.375, y*GRIDSIZE + GRIDSIZE*0.375))



 
justpressed = 0
def userinputs(k):
    global justpressed
    if justpressed == 1 and pygame.mouse.get_pressed()[0] == False:
        justpressed = 0
    if pygame.mouse.get_pressed()[0] == True and justpressed == 0:
        justpressed = 1
        k.recursiveshell()
        #opt,x,y=k.solverl1()
        #k.answers[x][y]=list(opt)[0]
        #print(k.legal(x,y))   
                
running = True
k = Kakuro(10,10)
#k.generator()
#k.constraintcreator()
k.loadingscreen()
#options, x, y = k.solverl1()
#print(f"{options}is the best at ({x}|{y})")


createKakuro(k)
#k.bsp()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        keypressed(k)
    screen.fill((0, 0, 0))
    mouse(k)
      
    drawgrid()
    drawvalue(k)
    #userinputs(k)
    pygame.display.flip()
    

pygame.quit()