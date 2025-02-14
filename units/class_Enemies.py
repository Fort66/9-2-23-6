from pygame.sprite import Sprite
from pygame.transform import rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed
import math

from icecream import ic

from config.create_Objects import screen

from config.sources.enemies.source import ENEMIES
from units.class_Shots import Shots


from random import randint, choice, uniform



class Enemies(Sprite):
    def __init__(
                self,
                group=None,
                player=None
                ):
        super().__init__(group)

        self.group = group
        self.player = player
        self.angle = 0
        self.rotation_speed = 10
        self.shots = False
        self.min_distance = 300
        self.shot_distance = 1500
        self.is_min_distance = False
        self.__post_init__()
        self.group.add(self)



    def __post_init__(self):
        self.image = ENEMIES[0]

        self.pos = (
                    uniform(
                        self.group.background_rect.left + 200,
                        self.group.background_rect.right - 200
                            ),
                    uniform(
                            self.group.background_rect.top + 200,
                            self.group.background_rect.bottom - 200
                            )
                    )


        self.random_value()
        self.check_move_count()
        self.change_direction()

        self.image_rotation = self.image.copy()
        self.rect = self.image_rotation.get_rect(center=self.pos)
        self.direction = Vector2(self.pos)



    def rotation(self):
        rotateX = self.player.rect.centerx - self.rect.centerx
        rotateY = self.player.rect.centery - self.rect.centery
        angle_vector = -math.atan2(rotateY, rotateX) * 180 / math.pi

        if angle_vector > 0:
            self.angle = angle_vector
        else:
            self.angle = 360 + angle_vector

        for value in ENEMIES:
            if self.angle <= value:
                self.image = ENEMIES[value]
                break

        self.image_rotation = self.image.copy()
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)


    def random_value(self):
        self.speed = randint(0, 10)
        self.direction_list = [0, 1, -1]
        self.move_count = randint(0, 600)


    def check_move_count(self):
        if self.move_count <= 0:
            self.random_value()
        else:
            self.move_count -= 1


    def change_direction(self):
        self.moveX = choice(self.direction_list)
        self.moveY = choice(self.direction_list)


    def check_position(self):
        if self.rect.left < self.group.background_rect.left:
            self.rect.left = self.group.background_rect.left
            self.change_direction()
        if self.rect.right > self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
            self.change_direction()
        if self.rect.top < self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
            self.change_direction()
        if self.rect.bottom > self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom
            self.change_direction()

        if not self.is_min_distance:
            if Vector2(self.rect.center).distance_to(self.player.rect.center) <= self.min_distance:
                self.is_min_distance = True
                self.change_direction()

        if Vector2(self.rect.center).distance_to(self.player.rect.center) > self.min_distance:
                self.is_min_distance = False


    def move(self):
        self.rect.move_ip(self.moveX * self.speed, self.moveY * self.speed)


    def shot(self):
        if randint(0, 100) == 50:
            self.group.add(
                            Shots(
                                pos=self.rect.center,
                                screen=screen,
                                group=self.group,
                                speed=10,
                                angle=self.angle,
                                kill_shot_distance=2000,
                                shoter=self,
                                color='yellow'
                                )
                            )



    def update(self):
        self.check_position()
        self.rotation()
        self.check_move_count()
        self.move()
        self.shot()