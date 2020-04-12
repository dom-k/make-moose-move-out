from enum import Enum
import pygame as pg
from settings import *
from spritesheet import Spritesheet
vec2 = pg.math.Vector2

class CharacterState(Enum):
    IDLE = 0
    ANGRY = 1
    HIT = 2

class AnimalCrossingCharacter(pg.sprite.Sprite):
    def __init__(self, game, pos_x, pos_y):
        self.game = game
        groups = game.all_sprites, game.character_sprites
        pg.sprite.Sprite.__init__(self, groups)
        self.pos = vec2(pos_x, pos_y)
        self.health = 100
        self.moving_out_counter = 0
        self.moving_out_wait_start_time = None
        self.moved_out = False
        self._idle_sprites = []
        self._hit_sprites = []
        self._angry_sprites = []
        self._spritesheet_file = 'assets/moose.png' 
        self._spritesheet = Spritesheet(self._spritesheet_file)
        self._load_default_sprite()
        self._load_sprites()
        self.rect = self.image.get_rect(topleft=self.pos)
        self.state = CharacterState.IDLE
        self._animation_counter = 0
        self._animation_index = 0
        self._hit_animation_counter = 0
        self._angry_animation_counter = 0

    def _load_default_sprite(self):
        self.image = self._spritesheet.get_image((0, 0), ((32, 32)))
        self.image.set_colorkey(BLACK)
        self.image = pg.transform.scale(self.image, (400, 400))


    def _load_sprites(self):
        sprite_size = (32, 32)
        self._idle_sprites.append(self._spritesheet.get_image((0, 0), sprite_size))
        self._idle_sprites.append(self._spritesheet.get_image((0, 32), sprite_size))

        self._hit_sprites.append(self._spritesheet.get_image((0, 64), sprite_size))

        self._angry_sprites.append(self._spritesheet.get_image((0, 96), sprite_size))
        self._angry_sprites.append(self._spritesheet.get_image((0, 128), sprite_size))
        self._angry_sprites.append(self._spritesheet.get_image((0, 160), sprite_size))

    def update(self):
        self._update_active_sprite()

        if self.health <= 0 and not self.moved_out:
            self.state = CharacterState.ANGRY
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

    def get_hit(self, damage):
        self.health -= damage
        self.state = CharacterState.HIT

    def _update_active_sprite(self):
        if self._animation_counter >= 60:
            if self.state == CharacterState.IDLE:
                self.image = self._idle_sprites[self._animation_index % len(self._idle_sprites)]
            elif self.state == CharacterState.ANGRY:
                self.image = self._angry_sprites[self._animation_index % len(self._angry_sprites)]
                self._angry_animation_counter += 1
                if self._angry_animation_counter >= 8:
                    self.state = CharacterState.IDLE
                    self._angry_animation_counter= 0

            elif self.state == CharacterState.HIT:
                self.image = self._hit_sprites[self._animation_index % len(self._hit_sprites)]
                self._hit_animation_counter += 1
                if self._hit_animation_counter >= 2:
                    self.state = CharacterState.IDLE
                    self._hit_animation_counter = 0
            self.image = pg.transform.scale(self.image, (400, 400))
            self._animation_index += 1
            self._animation_counter = 0
        else:
            self._animation_counter += 2

    def handle_event(self, event):
        pass
