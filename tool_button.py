import pygame as pg
vec2 = pg.math.Vector2

class ToolButton(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y, color, name):
        self.game = game
        groups = game.all_sprites, game.tool_sprites
        pg.sprite.Sprite.__init__(self, groups)
        self.pos = vec2(pos_x, pos_y)
        self.image = pg.Surface((100, 100))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=self.pos)
        self.name = name
        self.damage = 0

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            pos = pg.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.action()

    def action(self):
        pass

    def update(self):
        pass
