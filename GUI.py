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
k.bfill()
k.contentx[0][1] = 13
k.contentx[0][2] = 10
k.contentx[1][3] = 10
k.contentx[2][4] = 26
k.contentx[0][4] = "B"
k.contentx[0][5] = 43
k.contentx[0][6] = 15
k.contentx[1][7] = 8
k.contentx[0][8] = 8
k.contentx[0][9] = 14
k.contentx[5][1] = 6
k.contentx[5][2] = 24
k.contentx[5][3] = 17
k.contentx[6][6] = 8
k.contentx[5][7] = 14
k.contentx[5][8] = 23
k.contentx[5][9] = 6
k.contentx[4][1] = "B"
k.contentx[4][2] = "B"
k.contentx[8][3] = "B"

k.contenty[1][0] = 5
k.contenty[2][0] = 12
k.contenty[3][1] = 27
k.contenty[6][0] = 32
k.contenty[7][0] = 17
k.contenty[8][0] = 11
k.contenty[4][3] = 4
k.contenty[5][3] = 17
k.contenty[1][4] = 12
k.contenty[2][4] = 35
k.contenty[1][7] = 3
k.contenty[3][6] = 6
k.contenty[8][7] = 7
k.contenty[8][4] = 5
k.contenty[7][4] = 32
k.contenty[6][6] = 20
k.contenty[4][6] = "B"
k.contenty[5][6] = "B"
k.contenty[4][7] = "B"
k.contenty[4][8] = "B"
k.contenty[4][9] = "B"

print(k.getrowlength("right",1,1))

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