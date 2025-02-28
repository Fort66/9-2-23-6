import pygame as pg
from pygame.display import get_surface
from pygame.image import load
from pygame.sprite import Group
from pygame.math import Vector2

from config.create_Objects import levels_game
from functions.function_load_source import load_source

pg.init()



class CameraGroup(Group):
    def __init__(self, game=None):
        super().__init__(self)

        self.game = game
        self.display_surface = get_surface()
        self.offset = Vector2()
        self.half = (
            self.display_surface.get_size()[0] // 2,
            self.display_surface.get_size()[1] // 2,
        )
        self.camera_rect = pg.Rect(10, 10, 10, 10)
        self.set_background()

    def set_background(self):
        self.source = load_source(
            dir_path='config/sources/backgrounds',
            level=levels_game.game_level,
            current_level=levels_game.current_level
        )
        self.background_surface = load(self.source).convert_alpha()
        self.background_rect = self.background_surface.get_rect()

    def camera_center(self, target):
        self.offset.x = target.rect.centerx - self.half[0]
        self.offset.y = target.rect.centery - self.half[1]

    def custom_draw(self, player):
        self.camera_center(player)

        self.background_offset = self.background_rect.topleft - self.offset
        self.display_surface.blit(self.background_surface, self.background_offset)

        for sprite in sorted(self.sprites(), key=lambda sprite: sprite.rect.center):
            offset_position = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image_rotation, offset_position)

        self.game.mini_map.update()
