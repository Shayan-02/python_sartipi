import pygame as pg
from pygame.locals import *
import random
import sys

pg.init()
width = 800
height = 600
win = pg.display.set_mode((width, height))
pg.display.set_caption("Game")
clock = pg.time.Clock()


choices = [60, 1000]
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
c = (0, 255, 255)
firoozeee = (37, 190, 153)
white = (255, 255, 255)
black = (0, 0, 0)
x_rect = 350
y_rect = 500
speed = 1
fps = random.choice(choices)

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    win.fill(white)
    pg.draw.rect(win, firoozeee, ((x_rect, y_rect), (100, 100)))
    if x_rect > 0 and y_rect == 500:
        x_rect -= speed
    if x_rect == 0 and y_rect == 500:
        x_rect += -speed
    # if y_rect <= 500 and x_rect == 700:
    #     x_rect += -speed
    if event.type == KEYUP:
        if event.key == K_UP:
            speed += 1
        if event.key == K_DOWN:
            speed -= 1
    pg.display.update()
    clock.tick(fps)
pg.quit()
sys.exit()
