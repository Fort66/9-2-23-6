import pygame as pg

from config.create_Objects import screen
from classes.class_CheckEvents import CheckEvents
from classes.class_CameraGroup import CameraGroup
from units.class_Player import Player
from units.class_Enemies import Enemies


class Game:
    def __init__(self):
        self.run = True
        self.clock = pg.time.Clock()
        self.fps = 100
        self.check_events = CheckEvents(self)
        self.screen = screen
        self.create_groups()
        self.setup()


    def setup(self):
        self.player = Player(
                            pos=(self.screen.rect.center),
                            group=self.camera_group
                            )

        for _ in range(10):
            self.camera_group.add(
                                Enemies(
                                    group=self.camera_group,
                                    player=self.player
                                        )
                                )



    def create_groups(self):
        self.camera_group = CameraGroup(self)



    def run_game(self):
        while self.run:
            screen.window.fill(screen.color)

            self.check_events.check_events()


            self.camera_group.update()
            self.camera_group.custom_draw(self.player)


            self.screen.update_caption(f'{str(round(self.clock.get_fps(), 2))}')
            pg.display.update()
            self.clock.tick(self.fps)
