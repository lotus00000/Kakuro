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
     

def drawgrid():
    
    for x in range(0, WIDTH, GRIDSIZE):
        for y in range(0, HEIGHT, GRIDSIZE):
            rect = pygame.Rect(x, y, GRIDSIZE, GRIDSIZE)
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

running = True
k = Kakuro(9,10)
k.bsp()
print(k.getrowlength("right",6,5))
print(k.getrowvalue("right",6,5))


createKakuro(k)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0, 0, 0))  
    drawgrid()
    drawvalue(k)
    pygame.display.flip()
    

pygame.quit()