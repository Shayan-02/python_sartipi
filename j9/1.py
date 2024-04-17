import pygame as pg
import sys
from pygame.locals import *

pg.init()
width = 800
height = 600
cat_x = 500
cat_y = 400
speed = 5
win = pg.display.set_mode((width, height))
pg.display.set_caption("Game")
bg = pg.image.load("a.jpg")
BG = pg.transform.scale(bg, (width, height))
char = pg.image.load("cat.png")
CHAR = pg.transform.scale(char, (70, 70))


while True:
    win.blit(BG, (0, 0))
    win.blit(CHAR, (cat_x, cat_y))
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
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
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                cat_x += speed
            if event.key == K_LEFT:
                cat_x -= speed
        if event.type == KEYUP:
            if event.key == K_UP:
                cat_y -= speed
            if event.key == K_DOWN:
                cat_y += speed


    pg.display.update()

