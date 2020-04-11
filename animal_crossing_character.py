import pygame as pg
from settings import *
vec2 = pg.math.Vector2

MOOSE_COLOR = (132, 157, 210)

class AnimalCrossingCharacter(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        self.game = game
        groups = game.all_sprites, game.character_sprites
        pg.sprite.Sprite.__init__(self, groups)
        self.pos = vec2(pos_x, pos_y)
        self.image = pg.Surface((400, 400))
        self.image.fill(MOOSE_COLOR)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.health = 100

    def update(self):
        pass

    def handle_event(self, event):
        pass
