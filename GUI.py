from gamelogic import Kakuro
import pygame
pygame.init()
fontsize = 25
font = pygame.font.Font(None, fontsize)
color = (255, 255, 255)
GRIDSIZE = 75
BORDER = 5 #maximal GRIDSIZE/2
def createKakuro(kakuro):
    global WIDTH 
    WIDTH = kakuro.x*GRIDSIZE
    global HEIGHT 
    HEIGHT = kakuro.y*GRIDSIZE
     

def drawgrid(k):
    
    for x in range(0, WIDTH, GRIDSIZE):
        for y in range(0, HEIGHT, GRIDSIZE):
            rect = pygame.Rect(x, y, GRIDSIZE, GRIDSIZE)
            pygame.draw.rect(screen, color, rect, 1)
            drawvalue(k,x,y)

def drawvalue(kakuro, x, y):
    xcon = kakuro.contentx[x//GRIDSIZE][y//GRIDSIZE]
    ycon = kakuro.contenty[x//GRIDSIZE][y//GRIDSIZE]
    if (xcon!=0 and xcon!="B" ):
        text = font.render(f"{xcon}", True, color)                                                                   #vllt muss x,y // GRIDSIZE
        screen.blit(text,(x+GRIDSIZE*0.75,y+GRIDSIZE*0.375))
    if (ycon!=0 and ycon!="B"):
        text = font.render(f"{ycon}", True, color)                                                                   #vllt muss x,y // GRIDSIZE
        screen.blit(text,(x+GRIDSIZE*0.375,y+GRIDSIZE*0.75))
    elif(xcon == 0 and ycon == 0):
        rect = pygame.Rect(x+BORDER, y+BORDER, GRIDSIZE-2*BORDER, GRIDSIZE-2*BORDER)
        pygame.draw.rect(screen, color, rect)

running = True
k = Kakuro(10,10)
#k.bfill()
k.setcontentmanual([ #ChatGPT visualisierungbeispiel
 [0, 0, 23, 0, 0, 16, 0, 0, 0, 0],
 [0, 14, 0, 0, 0, 0, 0, 18, 0, 0],
 [0, 0, 0, 12, 0, 0, 25, 0, 0, 0],
 [9, 0, 0, 0, 0, 17, 0, 0, 0, 11],
 [0, 0, 20, 0, 0, 0, 0, 0, 13, 0],
 [0, 8, 0, 0, 0, 0, 19, 0, 0, 0],
 [0, 0, 0, 15, 0, 0, 0, 0, 0, 0],
 [0, 0, 22, 0, 0, 0, 0, 14, 0, 0],
 [10, 0, 0, 0, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 18, 0, 0, 0, 21, 0]
],
[
 [0, 0, 0, 19, 0, 0, 13, 0, 0, 0],
 [0, 0, 17, 0, 0, 21, 0, 0, 0, 0],
 [12, 0, 0, 0, 0, 0, 0, 16, 0, 0],
 [0, 15, 0, 0, 0, 0, 0, 0, 20, 0],
 [0, 0, 0, 0, 14, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 18, 0, 0, 0, 0],
 [0, 11, 0, 0, 0, 0, 0, 0, 0, 17],
 [0, 0, 0, 13, 0, 0, 0, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 22, 0, 0, 0],
 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])
createKakuro(k)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  
    drawgrid(k)
    pygame.display.flip()

pygame.quit()