import pygame, sys
from pygame.locals import *
pygame.init()

width = 800
height = 600
cat_x = 500
cat_y = 400
speed = 5
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game")
bg = pygame.image.load("a.jpg")
BG = pygame.transform.scale(bg, (width, height))
char = pygame.image.load("cat.png")
CHAR = pygame.transform.scale(char, (70, 70))


while True:
    win.blit(BG, (0, 0))
    win.blit(CHAR, (cat_x, cat_y))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_d:
                cat_x += speed
            if event.key == K_a:
                cat_x -= speed
        if event.type == KEYUP:
            if event.key == K_w:
                cat_y -= speed
            if event.key == K_s:
                cat_y += speed

    pygame.display.update()
