from gamelogic import Kakuro
import pygame
pygame.init()
fontsize = 25
font = pygame.font.Font(None, fontsize)
color = (255, 255, 255)
GRIDSIZE = 75
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
   
    text = font.render(f"{kakuro.contentx[x//GRIDSIZE][y//GRIDSIZE]}", True, color)                                                                   #vllt muss x,y // GRIDSIZE
    screen.blit(text,(x+GRIDSIZE*0.75,y+GRIDSIZE*0.375))
    text = font.render(f"{kakuro.contenty[x//GRIDSIZE][y//GRIDSIZE]}", True, color)                                                                   #vllt muss x,y // GRIDSIZE
    screen.blit(text,(x+GRIDSIZE*0.375,y+GRIDSIZE*0.75))

running = True
k = Kakuro(10,10)
k.bfill()
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