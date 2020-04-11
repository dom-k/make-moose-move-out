import pygame as pg
from tool_button import ToolButton

class MegaphoneToolButton(ToolButton):
    def __init__(self, game, pos_x, pos_y, color, name):
        super(MegaphoneToolButton, self).__init__(game, pos_x, pos_y, color, name)
        self.damage = 3

    def action(self):
        print('[%s] Hit mosse hard with %d damage' % (self.name, self.damage))
