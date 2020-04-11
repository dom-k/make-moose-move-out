import pygame as pg
vec2 = pg.math.Vector2

class HealthBar(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, color):
        self.game = game
        groups = game.all_sprites, game.character_sprites
        pg.sprite.Sprite.__init__(self, groups)
        self.pos = vec2(pos_x, pos_y)
        self.image = pg.Surface((400, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=self.pos)

    def update(self):
        self._update_with_character_health()

    def _update_with_character_health(self):
        if self.game.moose.health < 0:
            new_width = 0
        else:
            new_width = self.rect.width = self.game.moose.health * 4
        self.image = pg.transform.scale(self.image, (new_width, 50))

    def handle_event(self, event):
        pass

