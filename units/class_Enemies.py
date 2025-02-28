from pygame.sprite import Sprite
from pygame.transform import rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed
import math

from icecream import ic
from time import time

from config.create_Objects import (
    screen,
    checks,
    weapons,
    )

from config.sources.enemies.source import ENEMIES
from units.class_Shots import Shots
from units.class_Guardian import Guardian
from classes.class_SpriteGroups import SpriteGroups
from functions.function_enemies_collision import enemies_collision


from random import randint, choice, uniform


class Enemies(Sprite):
    def __init__(self, player=None):
        self.sprite_groups = SpriteGroups()
        super().__init__(self.sprite_groups.camera_group)
        self.sprite_groups.enemies_group.add(self)

        self.player = player
        self.angle = 0
        self.rotation_speed = 10
        self.shots = False
        self.min_distance = 300
        self.shot_distance = 1500
        self.is_min_distance = False
        self.shot_time = 0
        self.hp = 2
        self.__post_init__()


    def __post_init__(self):
        self.image = ENEMIES[1]["angle"][0]["sprite"]

        self.pos = (
            uniform(
                self.sprite_groups.camera_group.background_rect.left + 200,
                self.sprite_groups.camera_group.background_rect.right - 200,
            ),
            uniform(
                self.sprite_groups.camera_group.background_rect.top + 200,
                self.sprite_groups.camera_group.background_rect.bottom - 200,
            ),
        )

        self.random_value()
        self.check_move_count()
        self.change_direction()

        self.image_rotation = self.image.copy()
        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.direction = Vector2(self.pos)

        self.sprite_groups.enemies_group.add(shield := Guardian(
            dir_path="images/guards/guard2",
            speed_frames=0.09,
            scale_value=(1, 1),
            loops=-1,
            guard_level=randint(3, 10),
            size=self.rect.size,
            obj=self,
            angle=self.angle,
            owner=self
        ))
        self.sprite_groups.enemies_guard_group.add(shield)

        self.prepare_weapon(0)

    def prepare_weapon(self, angle):
        weapons.load_weapons(obj=self, source=ENEMIES[1]["angle"][angle]["weapons"], angle=angle)

    def pos_weapons_rotation(self):
        return weapons.pos_rotation(obj=self, angle=self.angle)

    def rotation(self):
        rotateX = self.player.rect.centerx - self.rect.centerx
        rotateY = self.player.rect.centery - self.rect.centery
        angle_vector = -math.atan2(rotateY, rotateX) * 180 / math.pi

        if angle_vector > 0:
            self.angle = angle_vector
        else:
            self.angle = 360 + angle_vector

        for value in ENEMIES[1]["angle"]:
            if self.angle <= value:
                self.image = ENEMIES[1]["angle"][value]["sprite"]
                self.prepare_weapon(value)
                break

        self.image_rotation = self.image.copy()
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)

    def random_value(self):
        self.speed = randint(0, 5)
        self.direction_list = [0, 1, -1]
        self.move_count = randint(0, 600)
        self.permission_shot = uniform(1, 3)

    def check_move_count(self):
        if self.move_count <= 0:
            self.random_value()
        else:
            self.move_count -= 1

    def change_direction(self):
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)

    def check_position(self):
        checks.position(self, self.sprite_groups.camera_group.background_rect)
        if not checks.resolved_move:
            self.change_direction()

        if not self.is_min_distance:
            if (
                Vector2(self.rect.center).distance_to(self.player.rect.center)
                <= self.min_distance
            ):
                self.is_min_distance = True
                self.change_direction()

        if (
            Vector2(self.rect.center).distance_to(self.player.rect.center)
            > self.min_distance
        ):
            self.is_min_distance = False

    def move(self):
        self.rect.move_ip(self.moveX * self.speed, self.moveY * self.speed)

    def shot(self):
        if (
            Vector2(self.rect.center).distance_to(self.player.rect.center)
            <= self.shot_distance
        ):
            if self.player.first_shot:
                if self.shot_time == 0:
                    self.shot_time = time()
                if time() - self.shot_time >= self.permission_shot:
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
                                color="yellow",
                                image="images/rockets/shot1.png",
                                scale_value=0.08,
                                owner=self
                            )
                        )
                        self.sprite_groups.enemies_shot_group.add(shot)
                        self.shot_time = time()

    def decrease_hp(self, value):
        if self.hp > 0:
            self.hp -= value
        if self.hp <= 0:
            self.kill()

    def update(self):
        self.check_position()
        self.rotation()
        self.check_move_count()
        self.move()
        self.shot()

        weapons.update_weapons(self, self.angle)
        enemies_collision()
