import pygame as pg
import sys

pg.init()

height = 600
width = 800

win = pg.display.set_mode((height, width))

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
firoozeee = (37, 190, 153)
white = (255, 255, 255)
black = (0, 0, 0)
text = "game"
font = pg.font.Font(None, 50)
win.fill(firoozeee)
pg.draw.rect(win, red, ((400, 300), (100, 50)), 1000)
pg.draw.circle(win, white, (300, 250), 20, 2)
pg.draw.ellipse(win, blue, ((500, 450), (100, 50)))
pg.draw.polygon(win, (255, 255, 0), ((100, 50), (200, 50), (175, 100), (75, 100)))
pg.draw.arc(win, (100, 100, 100), ((600, 100), (50, 50)), 1, 3)
pg.draw.line(win, red, (100, 200), (200, 200), 1)
pg.draw.lines(win, green, True, ((300, 300), (270, 310), (350, 350)))
pg.draw.aaline(win, blue, (50, 100), (150, 100), 1)

# img = pg.image.load("cat.png")
# pg.display.set_icon(img)
# bg = pg.image.load("bg.jpg")
# BG = pg.transform.scale(bg, (height, width))
# win.blit(bg, (0, 0))
# img1 = pg.image.load("bg.jpg")
# win.blit(img1, (0, 0))

t_s = font.render(text, True, (100, 0, 200))
win.blit(t_s, (600, 300))

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        pg.display.update()
pg.quit()
sys.exit()
