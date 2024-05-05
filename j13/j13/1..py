import pygame, sys, random
from pygame.locals import *

pygame.init()

# variables

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
yellow = (255, 255, 0)
gray = (30, 30, 30)
fps = 10
win_width = 800
win_height = 600
worm_x = 380
worm_y = 280
worm_x_speed = 0
worm_y_speed = 0
food_x = random.randrange(0, 780, 20)
food_y = random.randrange(0, 580, 20)
worm_list = []
worm_length = 0
game_over = False
a = ["r", "l", "u", "d"]

win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("SnakeGame")
clock = pygame.time.Clock()


def worm_function(worm_lst, wrm_x, wrm_y):
    g_over = False
    worm_head = [wrm_x, wrm_y]
    worm_lst.append(worm_head)
    for lst in worm_lst:
        pygame.draw.rect(win, green, (lst[0], lst[1], 20, 20))
    for each_section in worm_lst[:-1]:
        if each_section == worm_head:
            g_over = True
    return g_over


while not game_over:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT and "l" in a:
                worm_x_speed = -20
                worm_y_speed = 0
                a.clear()
                a.append("l")
                a.append("u")
                a.append("d")
            elif event.key == K_RIGHT and "r" in a:
                worm_x_speed = 20
                worm_y_speed = 0
                a.clear()
                a.append("r")
                a.append("u")
                a.append("d")
            elif event.key == K_UP and "u" in a:
                worm_y_speed = -20
                worm_x_speed = 0
                a.clear()
                a.append("r")
                a.append("l")
                a.append("d")
            elif event.key == K_DOWN and "d" in a:
                worm_y_speed = 20
                worm_x_speed = 0
                a.clear()
                a.append("r")
                a.append("u")
                a.append("l")
    worm_x += worm_x_speed
    worm_y += worm_y_speed
    if worm_x < 0:
        worm_x = 780
    if worm_x > 780:
        worm_x = 0
    if worm_y < 0:
        worm_y = 580
    if worm_y > 580:
        worm_y = 0
    if worm_x == food_x and worm_y == food_y:
        food_x = random.randrange(0, 780, 20)
        food_y = random.randrange(0, 580, 20)
        worm_length += 1
    if len(worm_list) > worm_length:
        worm_list.pop(0)
    win.fill(black)
    if worm_function(worm_list, worm_x, worm_y):
        game_over = True
    pygame.draw.rect(win, red, (food_x, food_y, 20, 20))
    pygame.display.update()
    clock.tick(fps)
