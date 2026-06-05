from gamelogic import *
import math
import sys
import random
import threading
import time
#sys.setrecursionlimit(5000)
import pygame
pygame.init()
background = (0,0,0)
fontsize = 25
font = pygame.font.Font(None, fontsize)
secc = False
pygame.display.set_caption("-------------------------------------------------------------PRESS R TO START------------------------------------")
blank = pygame.Surface((32, 32), pygame.SRCALPHA)
pygame.display.set_icon(blank)
color = (255,255,255)
colorpressed = (255,0,0)
GRIDSIZE = 75
BORDER = 10 #maximal GRIDSIZE/2
state3 = True #entscheidet ob es am Anfang ein eindeutig lösbares Feld zum einstieg geben muss, False bedeutet es ist eindeutig

#-------------------------------
    
    #AUTHOR: ALEXANDER PETRI

    #USER MANUAL
    #BELOW ALL COMMANDS ARE LISTED
    # C - CHECK A PUZZLES LEGALITY
    # R - GENERATE A PUZZLE
    # Q - GET A HINT
    # W - WIPE ALL ANSWERS
    # S - SOLVE PUZZLE
    # SPACE - REMOVE SINGLE ANSWER

#-------------------------------

k = Kakuro(10,10,50,24,4,1)

#-------------------------------
#Rechenaufwändig jedoch einfach lösbare Puzzel, die schaffen auch Sie

#-------------------------------

#k = Kakuro(10,10,200,23,5,7)

#-------------------------------
#schneller,härter , der Computer hat kein Problem damit

#-------------------------------

#k = Kakuro(10,10,400,15,5,10)

#-------------------------------
#superschnell, extrem, menschlich sogut wie unlösbar

#k = Kakuro(10,10,100,0,4,10)

#-------------------------------
#ausgelegt für schnelle generation "Augenblick"



def createKakuro(kakuro):
    global WIDTH 
    WIDTH = kakuro.x*GRIDSIZE
    global HEIGHT 
    HEIGHT = kakuro.y*GRIDSIZE

clicked = () 
clicked2 = ()
def mouse(k):
    global clicked
    global clicked2
    if pygame.mouse.get_pressed()[0]==True:
        x,y = pygame.mouse.get_pos()
        if x<WIDTH and y<HEIGHT:
            x,y = math.floor(x/GRIDSIZE), math.floor(y/GRIDSIZE)
            if k.contenty[x][y] == 0 and k.contentx[x][y] == 0 or x+y==0:
                clicked = (x,y)  
            clicked2=(x,y)

stop_event = threading.Event()
def timer():
    time.sleep(2)
    stop_event.set()

def keypressed(k):
    global clicked
    global secc

    if event.type == pygame.KEYDOWN:
        if pygame.K_1 <= event.key <= pygame.K_9:
            if clicked != None:
                k.answers[clicked[0]][clicked[1]] = event.unicode
                secc = False

        elif pygame.K_s == event.key:
            k.wipeanswers()
            k.recursiveshell()

        elif pygame.K_q == event.key:
            options, x, y = k.solverl1()
            if x+y!=0 and secc==False:
                clicked = x,y
                secc = True
                #pygame.display.set_caption(f"{options}is the best at marked")#({x}|{y})")
            elif x+y!=0 and secc==True:
                k.answers[x][y] = next(iter(options))
                secc = False
        elif pygame.K_c == event.key:
            b = 0   
            for x in range(len(k.answers)):
                for y in range(len(k.answers[0])):
                    if k.answers[x][y]!=0:
                        if k.legal(x,y)==False:
                            b = 1
                            print(f"Stelle ({x}|{y}) ist illegal")
            if b == 0:
                pygame.display.set_caption("puzzle is legal")
            else:
                pygame.display.set_caption("puzzle is illegal")

        elif pygame.K_SPACE == event.key:
            k.answers[clicked[0]][clicked[1]] = 0 

        elif pygame.K_r == event.key:
            generatepuzzle(k)
            
            
        elif pygame.K_w == event.key:
            k.wipeanswers()     
def generatepuzzle(k):
    
    pygame.display.set_caption("GENERATING...")
    global state3 
    global clicked
    state4 = False
    while not state4:
        state4 = state3
        state2 = False
        while not state2:
            state = False
            while not state:
                seed = random.randint(10**(k.seedlength-1),10**k.seedlength-1)
                k.wipeanswers()
                k.generator(seed)
                k.randomfill()
                k.sumup()
                k.wipeanswers()
                state, _ = k.recursiveshell()
                
                k.wipeanswers() 
            state2, _ = k.checksize()
            
        options, x, y = k.solverl1()
        if len(options)==1: state4=True
    pygame.display.set_caption(str(seed))
    print(str(seed))
    
    clicked = ()

def drawgrid():
    for x in range(0, WIDTH, GRIDSIZE):
        for y in range(0, HEIGHT, GRIDSIZE):
            rect = pygame.Rect(x, y, GRIDSIZE, GRIDSIZE)
            if clicked == (round(x/GRIDSIZE),round(y/GRIDSIZE)):
                
                pygame.draw.rect(screen, colorpressed, rect, 1)
            else:
                pygame.draw.rect(screen, color, rect, 1)
    rect = pygame.Rect(2*BORDER, 2*BORDER, GRIDSIZE-4*BORDER, GRIDSIZE-4*BORDER)
    pygame.draw.rect(screen, colorpressed, rect)        

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
            if(ycon == "?" and xcon=="?" and x+y==0):
                text = font.render("?", True, color)                                                                   #vllt muss x,y // GRIDSIZE
                screen.blit(text,(x*GRIDSIZE + GRIDSIZE*0.375, y*GRIDSIZE + GRIDSIZE*0.375))
            elif(xcon == 0 and ycon == 0):
                rect = pygame.Rect( x*GRIDSIZE + BORDER, y*GRIDSIZE + BORDER, GRIDSIZE - 2*BORDER, GRIDSIZE - 2*BORDER)
                pygame.draw.rect(screen, color, rect)
                if k.answers[x][y]!=0:
                    text = font.render(f"{k.answers[x][y]}", True, background)                                                                   #vllt muss x,y // GRIDSIZE
                    screen.blit(text,(x*GRIDSIZE + GRIDSIZE*0.375, y*GRIDSIZE + GRIDSIZE*0.375))
menu = False
def helpmenu():
    global menu
    global clicked

    if clicked == (0,0) and menu == False:
        menu = True
        time.sleep(0.2)
        clicked = ()

    if clicked == (0,0) and menu == True:
        menu = False
        time.sleep(0.2)
        clicked = ()
    

options=[]
for i in range(5):
    for j in range(8):
        if j!=6:
            options.append([i+1,j+1])

def colorpicker():
    global clicked
    global color
    global background
    global colorpressed 
    if clicked2 == (1,8):
        color = (255,255,255)
        background = (0,0,0)
        colorpressed = (255,0,0)
    if clicked2 == (2,8):
        background = (55,55,55)
        color = (255,153,0)
        colorpressed = (228,69,69)
    if clicked2 == (3,8):
        background = (50,52,55)
        color = (202,71,84)
        colorpressed = (248,212,7)
    if clicked2 == (4,8):
        background = (0,0,0)
        color = (3, 160, 98)  
        colorpressed = (248,212,7)  
    if clicked2 == (5,8):
        background = (0,0,0)
        color = (151,47,255)
        colorpressed = (248,212,7)


def drawgridmenu():
    global options
    for x in range(0, WIDTH, GRIDSIZE):
        for y in range(0, HEIGHT, GRIDSIZE):
            rect = pygame.Rect(x, y, GRIDSIZE, GRIDSIZE)
            
            if not [x/GRIDSIZE,y/GRIDSIZE] in options:
                if clicked == (round(x/GRIDSIZE),round(y/GRIDSIZE)):
                    
                    
                    pygame.draw.rect(screen, colorpressed, rect, 1)
                else:
                    pygame.draw.rect(screen, color, rect, 1)
            else:
                
                pygame.draw.rect(screen, (55,55,55), rect)
                if x/GRIDSIZE ==5 and y/GRIDSIZE == 8 :
                    pygame.draw.rect(screen, (151,47,255), rect)
                    rect = pygame.Rect(x+BORDER, y+BORDER, GRIDSIZE-2*BORDER, GRIDSIZE-2*BORDER)
                    pygame.draw.rect(screen, (0,0,0), rect)
                if x/GRIDSIZE ==4 and y/GRIDSIZE == 8 :
                    pygame.draw.rect(screen, ((3, 160, 98)), rect)
                    rect = pygame.Rect(x+BORDER, y+BORDER, GRIDSIZE-2*BORDER, GRIDSIZE-2*BORDER)
                    pygame.draw.rect(screen, (0,0,0), rect)
                if x/GRIDSIZE ==3 and y/GRIDSIZE == 8 :
                    pygame.draw.rect(screen, (202,71,84), rect)
                    rect = pygame.Rect(x+BORDER, y+BORDER, GRIDSIZE-2*BORDER, GRIDSIZE-2*BORDER)
                    pygame.draw.rect(screen, (50,52,55), rect)
                if x/GRIDSIZE ==2 and y/GRIDSIZE == 8 :
                    pygame.draw.rect(screen, (255,153,0), rect)
                    rect = pygame.Rect(x+BORDER, y+BORDER, GRIDSIZE-2*BORDER, GRIDSIZE-2*BORDER)
                    pygame.draw.rect(screen, (55,55,55), rect)
                if x/GRIDSIZE ==1 and y/GRIDSIZE == 8 :
                    pygame.draw.rect(screen, (255,255,255), rect)
                    rect = pygame.Rect(x+BORDER, y+BORDER, GRIDSIZE-2*BORDER, GRIDSIZE-2*BORDER)
                    pygame.draw.rect(screen, (0,0,0), rect)
    text = font.render("R - Generate Puzzle", True, color)    
    screen.blit(text,(2*GRIDSIZE + GRIDSIZE*0.375, 2*GRIDSIZE + GRIDSIZE*0.375))
    text = font.render("Q - Receive Hint", True, color)    
    screen.blit(text,(2*GRIDSIZE + GRIDSIZE*0.375, 3*GRIDSIZE + GRIDSIZE*0.375))
    text = font.render("S - Solve Puzzle", True, color)    
    screen.blit(text,(2*GRIDSIZE + GRIDSIZE*0.375, 4*GRIDSIZE + GRIDSIZE*0.375))
    text = font.render("W - Wipe Puzzle", True, color)    
    screen.blit(text,(2*GRIDSIZE + GRIDSIZE*0.375, 5*GRIDSIZE + GRIDSIZE*0.375))
    rect = pygame.Rect(2*BORDER, 2*BORDER, GRIDSIZE-4*BORDER, GRIDSIZE-4*BORDER)
    pygame.draw.rect(screen, color, rect)
 

        




k.loadingscreen()
createKakuro(k)

running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))
while running:

    mouse(k)
    helpmenu()
    
    if menu == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            keypressed(k)
        
        screen.fill(background)
        drawgrid()
        drawvalue(k)

    elif menu == True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        colorpicker()  
        screen.fill(background)
        drawgridmenu()
    pygame.display.flip()
    

pygame.quit()