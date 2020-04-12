import pygame as pg
from tool_button import ToolButton
from spritesheet import Spritesheet

class AxeToolButton(ToolButton):
    def __init__(self, game, pos_x, pos_y, color, name):
        super(AxeToolButton, self).__init__(game, pos_x, pos_y, color, name)
        spritesheet_file = 'assets/tools.png'
        spritesheet = Spritesheet(spritesheet_file)
        self.image = spritesheet.get_image((0, 0), (32, 32))
        self.image = pg.transform.scale(self.image, (100, 100))
        self.damage = 2

    def action(self):
        print('[%s] Hit mosse hard with %d damage' % (self.name, self.damage))
        self.game.moose.get_hit(self.damage)
