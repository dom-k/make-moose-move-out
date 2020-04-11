import sys
import pygame as pg
from tool_button import ToolButton

BGCOLOR = (40, 40, 40)
PURPLE = (200, 146, 248)
BLUE = (141, 159, 242)
RED = (233, 140, 91)
GREEN = (129, 194, 131)
FPS = 60

class GameManager:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((600, 800))
        pg.display.set_caption('make moose move out')
        pg.mouse.set_visible(1)
        self.clock = pg.time.Clock()
        self.all_sprites = pg.sprite.RenderPlain()
        self.tool_sprites = pg.sprite.RenderPlain()
        self._init_tool_buttons()

    def _init_tool_buttons(self):
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
            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                for sprite in self.tool_sprites:
                    sprite.handle_click(mouse_pos)
            elif event.type == pg.MOUSEBUTTONUP:
                pass

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.screen.fill(BGCOLOR)
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, sprite.pos)
        pg.display.flip()

    def quit(self):
        pg.quit()
        sys.exit()


def main():
    gamemanager = GameManager()
    gamemanager.run()

if __name__ == '__main__':
    main()
