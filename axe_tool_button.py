import pygame as pg
from tool_button import ToolButton

class AxeToolButton(ToolButton):
    def __init__(self, game, pos_x, pos_y, color, name):
        super(AxeToolButton, self).__init__(game, pos_x, pos_y, color, name)
        self.damage = 2

    def action(self):
        print('[%s] Hit mosse hard with %d damage' % (self.name, self.damage))
        self.game.moose.health -= self.damage
