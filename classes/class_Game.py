import pygame as pg

from config.create_Objects import screen
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from units.class_Player import Player
from units.class_Enemies import Enemies
from classes.class_SpriteGroups import SpriteGroups
from UI.screens.class_MiniMap import MiniMap


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.check_events = CheckEvents(self)
        self.screen = screen
        self.sprite_groups = SpriteGroups()
        self.sprite_groups.camera_group = CameraGroup(self)
        self.mini_map = MiniMap(scale_value=.2, color_map=(0, 100, 0, 150))
        self.setup()

    def setup(self):
        self.player = Player(pos=(self.screen.rect.center))

        for _ in range(10):
            self.sprite_groups.camera_group.add(Enemies(player=self.player))

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            self.sprite_groups.camera_group.update()
            self.sprite_groups.camera_group.custom_draw(self.player)

            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
