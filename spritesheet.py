import pygame as pg
from settings import BLACK
vec2 = pg.math.Vector2

class Spritesheet:
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()

    def get_image(self, pos, size):
        """ Grab an image out of the spritesheet. """
        image = pg.Surface(size)
        image.blit(self.spritesheet, (0, 0), (pos + size))
        image.set_colorkey(BLACK)
        return image
