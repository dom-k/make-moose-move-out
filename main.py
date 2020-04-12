import sys
import pygame as pg
from settings import *
from tool_button import ToolButton
from axe_tool_button import AxeToolButton
from net_tool_button import NetToolButton
from shovel_tool_button import ShovelToolButton
from megaphone_tool_button import MegaphoneToolButton
from mouse_pointer import MousePointer
from animal_crossing_character import AnimalCrossingCharacter
from health_bar import HealthBar
from dialogbox import DialogBox, EndDialogText

class GameManager:
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pg.display.set_caption(SCREEN_CAPTION)
        pg.mouse.set_visible(0)
        self.clock = pg.time.Clock()
        self._init_sprite_groups()
        self._load_game_objects()
        self._load_tool_buttons()

    def _init_sprite_groups(self):
        self.all_sprites = pg.sprite.RenderPlain()
        self.tool_sprites = pg.sprite.RenderPlain()
        self.character_sprites = pg.sprite.RenderPlain()
        self.text_sprites = pg.sprite.RenderPlain()
        self.core_sprites = pg.sprite.RenderPlain()

    def _load_game_objects(self):
        self.mouse_pointer = MousePointer(self)
        self.moose = AnimalCrossingCharacter(self, 100, 150)
        self.health_bar = HealthBar(self, 100, 50, (240, 240, 240))
        self.dialogbox = DialogBox(self, 100, 550, FGCOLOR)
        self.end_dialog_text = EndDialogText(self, 110, 560, BGCOLOR)

    def _load_tool_buttons(self):
        pos_y = 650
        self.net_button = NetToolButton(self, 25, pos_y, PURPLE, 'Net')
        self.axe_button = AxeToolButton(self, 175, pos_y, BLUE, 'Axe')
        self.shovel_button = ShovelToolButton(self, 325, pos_y, RED, 'Shovel')
        self.megaphone_button = MegaphoneToolButton(self, 475, pos_y, GREEN, 'Megaphone')

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
        self.character_sprites.draw(self.screen)
        self._draw_text()
        self.core_sprites.draw(self.screen) # Should be rendered last.
        pg.display.flip()

    def _draw_text(self):
        for sprite in self.text_sprites:
            if sprite.show_text:
                self.screen.blit(sprite.image, sprite.pos)

    def quit(self):
        pg.quit()
        sys.exit()


def main():
    gamemanager = GameManager()
    gamemanager.run()

if __name__ == '__main__':
    main()
