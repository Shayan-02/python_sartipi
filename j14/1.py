import random

import pygame as pg
from pygame.math import Vector2


class Projectile(pg.sprite.Sprite):

    def __init__(self, pos, game_area):
        super().__init__()
        self.image = pg.Surface((5, 5))
        self.image.fill(pg.Color("aquamarine2"))
        self.rect = self.image.get_rect(center=pos)
        self.vel = Vector2(2, 0).rotate(random.randrange(360))
        self.pos = Vector2(pos)
        self.game_area = game_area

    def update(self):
        self.pos += self.vel
        self.rect.center = self.pos
        if not self.game_area.contains(self.rect):
            self.kill()


def main():
    screen = pg.display.set_mode((640, 480))
    game_area = pg.Rect(60, 60, 520, 360)
    game_area_color = pg.Color("aquamarine2")
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group(Projectile(game_area.center, game_area))

    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True

        all_sprites.add(Projectile(game_area.center, game_area))
        all_sprites.update()

        screen.fill((30, 30, 30))
        all_sprites.draw(screen)
        pg.draw.rect(screen, game_area_color, game_area, 2)

        pg.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
