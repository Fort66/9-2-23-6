import pygame as pg

from config.create_Objects import screen, levels_game
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from classes.class_SpriteGroups import SpriteGroups
from classes.class_BackgroundScreen import BackgroundScreen
from units.class_Player import Player
from units.class_Enemies import Enemies
from UI.screens.class_MiniMap import MiniMap


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.check_events = CheckEvents(self)
        self.screen = screen
        self.old_screen_size = self.screen.window.get_size()
        self.sprite_groups = SpriteGroups()
        self.sprite_groups.camera_group = CameraGroup(self)
        self.mini_map = MiniMap(scale_value=0.1, color_map=(0, 100, 0, 150))
        self.background_animate()
        self.setup()

    def setup(self):
        self.player = Player(pos=(self.screen.rect.center))

        for _ in range(levels_game.enemies_attack):
            self.sprite_groups.camera_group.add(Enemies(player=self.player))

    def check_screen_size(self):
        if self.old_screen_size != self.screen.window.get_size():
            self.background_animate()
            self.old_screen_size = self.screen.window.get_size()

    def background_animate(self):
        self.back_animate = BackgroundScreen(
            dir_path='images/back_animate/1',
            speed_frames=0.1,
            owner=self.screen,
            loops=-1,
            no_group=True,
            size=(
                self.screen.rect[2],
                self.screen.rect[3]
            )
        )

    def clear_player_group(self):
        self.sprite_groups.player_group.empty()
        self.sprite_groups.player_shot_group.empty()
        self.sprite_groups.player_guard_group.empty()

    def clear_enemies_group(self):
        self.sprite_groups.enemies_group.empty()
        self.sprite_groups.enemies_shot_group.empty()
        self.sprite_groups.enemies_guard_group.empty()

    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()

            self.check_screen_size()
            self.back_animate.update()
            self.sprite_groups.camera_group.update()

            self.screen.update_caption(f"{str(round(self.clock.get_fps(), 2))}")
            pg.display.update()
            self.clock.tick(self.fps)
