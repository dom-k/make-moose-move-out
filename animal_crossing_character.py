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
        # self.image = pg.Surface((400, 400))
        # self.image.fill(MOOSE_COLOR)
        self.image = pg.image.load('assets/moose_idle.png').convert()
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (400, 400))
        self.rect = self.image.get_rect(topleft=self.pos)
        self.health = 100
        self.moving_out_counter = 0
        self.moving_out_wait_start_time = None
        self.moved_out = False

    def update(self):
        if self.health <= 0 and not self.moved_out:
            self.game.end_dialog_text.show_text = True
            self.moving_out_wait_start_time = pg.time.get_ticks()
            self.moved_out = True

        if self.moving_out_wait_start_time and self.moved_out:
            time_since_start = pg.time.get_ticks() - self.moving_out_wait_start_time
            if time_since_start >= 5000:
                self.moved_out = False
                self.moving_out_counter += 1
                self.health = 100
                self.game.end_dialog_text.show_text = False
                self.moving_out_wait_start_time = 0

    def handle_event(self, event):
        pass
