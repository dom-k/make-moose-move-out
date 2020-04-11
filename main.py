import sys
import pygame as pg
from tool_button import ToolButton
from mouse_pointer import MousePointer

BGCOLOR = (40, 40, 40) # TODO: Make a settings.py file
PURPLE = (200, 146, 248)
BLUE = (141, 159, 242)
RED = (233, 140, 91)
GREEN = (129, 194, 131)
FPS = 60
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
CAPTION = 'make moose move out'

class GameManager:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(CAPTION)
        pg.mouse.set_visible(1)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.RenderPlain()
        self.tool_sprites = pg.sprite.RenderPlain()
        self.core_sprites = pg.sprite.RenderPlain() # Should be rendered last
        self._load_game_objects()
        self._load_tool_buttons()

    def _load_game_objects(self):
        self.mouse_pointer = MousePointer(self)

    def _load_tool_buttons(self):
        pos_y = 650
        self.net_button = ToolButton(self, 25, pos_y, PURPLE, 'Net')
        self.axe_button = ToolButton(self, 175, pos_y, BLUE, 'Axe')
        self.shovel_button = ToolButton(self, 325, pos_y, RED, 'Shovel')
        self.megaphone_button = ToolButton(self, 475, pos_y, GREEN, 'Megaphone')

    def run(self):
        while 1:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.quit()
            elif event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                self.quit()

            for sprite in self.all_sprites:
                sprite.handle_event(event)

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        self.tool_sprites.draw(self.screen)
        self.core_sprites.draw(self.screen)
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()


def main():
    gamemanager = GameManager()
    gamemanager.run()

if __name__ == '__main__':
    main()
