from pygame.sprite import Sprite
from pygame.transform import rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

from icecream import ic

import math
from time import time

from config.create_Objects import (
    screen,
    checks,
    weapons,
    )

from config.sources.heroes.source import HEROES
from units.class_Shots import Shots
from units.class_Guardian import Guardian
from classes.class_SpriteGroups import SpriteGroups

from functions.function_player_collision import player_collision


class Player(Sprite):
    def __init__(
        self,
        pos=None,
    ):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)
        self.sprite_groups.camera_group.add(self)
        self.sprite_groups.player_group.add(self)

        self.pos = pos
        self.direction = Vector2(pos)
        self.angle = 0
        self.rotation_speed = 10
        self.speed = 5
        self.shot_time = 1
        self.permission_shot = .25
        self.first_shot = False
        self.hp = 5
        self.__post_init__()

    def __post_init__(self):
        self.image = HEROES[1]["angle"][0]["sprite"]
        self.image_rotation = self.image.copy()
        self.rect = self.image_rotation.get_rect(center=self.pos)

        self.sprite_groups.camera_group.add(shield := Guardian(
            dir_path="images/guards/guard1",
            speed_frames=0.09,
            scale_value=(1, 1),
            loops=-1,
            guard_level=10,
            size=self.rect.size,
            obj=self,
            angle=self.angle,
            owner=self
        ))
        self.sprite_groups.player_guard_group.add(shield)

        self.prepare_weapon(0)


    def handle_event(self, event):
        if event.type == MOUSEWHEEL:
            if event.y == -1:
                self.angle = (self.angle - self.rotation_speed) % 360
                self.rotation()
            elif event.y == 1:
                self.angle = (self.angle + self.rotation_speed) % 360
                self.rotation()

        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:
                if not self.first_shot:
                    self.first_shot = not self.first_shot
                if self.shot_time == 0:
                    self.shot_time = time()
                if time() - self.shot_time >= self.permission_shot:
                    self.shot()
                    self.shot_time = time()

    def shot(self):
        value = self.pos_weapons_rotation()
        for pos in value:
            self.sprite_groups.camera_group.add(shot:=
                Shots(
                    pos=(pos),
                    screen=screen,
                    speed=8,
                    angle=self.angle,
                    kill_shot_distance=2000,
                    shoter=self,
                    image="images/rockets/shot3.png",
                    scale_value=0.15,
                    owner=self
                )
            )
            self.sprite_groups.player_shot_group.add(shot)

    def prepare_weapon(self, angle):
        weapons.load_weapons(obj=self, source=HEROES[1]["angle"][angle]["weapons"], angle=angle)

    def pos_weapons_rotation(self):
        return weapons.pos_rotation(obj=self, angle=self.angle)

    def rotation(self):
        for value in HEROES[1]["angle"]:
            if self.angle <= value:
                self.image = HEROES[1]["angle"][value]["sprite"]
                self.prepare_weapon(value)
                break

        self.image_rotation = self.image.copy()
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def check_position(self):
        checks.position(self, self.sprite_groups.camera_group.background_rect)

    def move(self):
        keys = get_pressed()
        if keys[K_a]:
            self.rect.move_ip(-self.speed, 0)
        if keys[K_d]:
            self.rect.move_ip(self.speed, 0)
        if keys[K_w]:
            self.rect.move_ip(0, -self.speed)
        if keys[K_s]:
            self.rect.move_ip(0, self.speed)

    def decrease_hp(self, value):
        if self.hp > 0:
            self.hp -= value
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.check_position()
        self.move()

        weapons.update_weapons(self, self.angle)
        player_collision()
