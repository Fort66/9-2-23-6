from pygame.sprite import Sprite
from pygame.transform import rotozoom, scale_by
from pygame.image import load
from pygame.locals import MOUSEWHEEL, MOUSEBUTTONDOWN, K_a, K_d, K_w, K_s
from pygame.math import Vector2
from pygame.key import get_pressed

from icecream import ic

from config.create_Objects import screen

from config.sources.heroes.source import HEROES
from units.class_Shots import Shots



class Player(Sprite):
    def __init__(
                self,
                pos=None,
                group=None,
                ):
        super().__init__(group)

        self.pos = pos
        self.group = group
        self.direction = Vector2(pos)
        self.angle = 0
        self.rotation_speed = 10
        self.speed = 7

        self.image = HEROES[0]
        self.image_rotation = self.image.copy()
        self.rect = self.image_rotation.get_rect(center=pos)
        self.group.add(self)


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
                self.shot()


    def shot(self):
        self.group.add(
                        Shots(
                            pos=self.rect.center,
                            screen=screen,
                            group=self.group,
                            speed=10,
                            angle=self.angle,
                            kill_shot_distance=2000,
                            shoter=self
                            )
                        )


    def rotation(self):
        for value in HEROES:
            if self.angle <= value:
                self.image = HEROES[value]
                break

        self.image_rotation = self.image.copy()
        self.image_rotation = rotozoom(self.image, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)


    def check_position(self):
        if self.rect.left < self.group.background_rect.left:
            self.rect.left = self.group.background_rect.left
        if self.rect.right > self.group.background_rect.right:
            self.rect.right = self.group.background_rect.right
        if self.rect.top < self.group.background_rect.top:
            self.rect.top = self.group.background_rect.top
        if self.rect.bottom > self.group.background_rect.bottom:
            self.rect.bottom = self.group.background_rect.bottom


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


    def update(self):
        self.check_position()
        self.move()