import pygame

WIDTH = 100
HEIGHT = 100
GRIDSIZE = 10

def drawgrid():
    global rectangle
    rectangle = []
    i = 0
    for x in range(0, WIDTH, GRIDSIZE):
        for y in range(0, HEIGHT, GRIDSIZE):
            rect = pygame.Rect(x, y, GRIDSIZE, GRIDSIZE)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)
            rectangle.append(rect)