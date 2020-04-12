import pygame as pg
from settings import FONT, FONT_SIZE
vec2 = pg.math.Vector2

class EndDialogText(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, color):
        groups = game.all_sprites, game.text_sprites
        pg.sprite.Sprite.__init__(self, groups)
        self.pos = vec2(pos_x, pos_y)
        self.text = 'FINE, I\'LL MOVE OUT!'
        self.font = pg.font.Font(FONT, FONT_SIZE)
        self.image = self.font.render(self.text, False, color)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.show_text = False

    def handle_event(self, event):
        pass

class DialogBox(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, color):
        self.game = game
        groups = game.all_sprites, game.character_sprites
        pg.sprite.Sprite.__init__(self, groups)
        self.pos = vec2(pos_x, pos_y)
        self.image = pg.Surface((400, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self):
        pass

    def handle_event(self, event):
        pass

