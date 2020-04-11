import pygame as pg
vec2 = pg.math.Vector2
from settings import BLACK

class MousePointer(pg.sprite.Sprite):
    def __init__(self, game):
        self.game = game
        groups = game.core_sprites, game.all_sprites
        pg.sprite.Sprite.__init__(self, groups)
        self.pos = (0, 0)
        self.image = pg.image.load('assets/mouse_pointer.png').convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.clicking = 0

    def update(self):
        self._follow_mouse_pos()

    def _follow_mouse_pos(self):
        self.rect.midtop = pg.mouse.get_pos()

        if self.clicking:
            self.rect.move_ip(5, 10)

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            self.clicking = 1
        elif event.type == pg.MOUSEBUTTONUP:
            self.clicking = 0

