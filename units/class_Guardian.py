from pygame.sprite import Sprite
from pygame.transform import rotozoom

from time import time
from classes.class_Animator import Animator
from functions.function_guards_collision import (
    player_guard_collision,
    enemies_guard_collision,
    guards_collision
    )


class Guardian(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frames=None,
        guard_level=None,
        scale_value=None,
        loops=None,
        size=None,
        angle=None,
        owner=None
    ):

        super().__init__(
            dir_path=dir_path,
            speed_frames=speed_frames,
            scale_value=scale_value,
            loops=loops,
            size=size,
        )

        self.guard_level = guard_level
        self.angle = angle
        self.owner = owner
        self.destruction_time = 0
        self.rect = self.image_rotation.get_rect(center=self.owner.rect.center)

    def decrease_level(self, value):
        if self.guard_level > 0:
            self.guard_level -= value


    def update(self):
        player_guard_collision()
        enemies_guard_collision()
        guards_collision()

        self.angle = self.owner.angle
        self.rect.center = self.owner.rect.center
        self.image_rotation = self.frames[self.frame][0]
        self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
        self.rect = self.image_rotation.get_rect(center=self.rect.center)
        super().animate()

        if guards_collision():
            if self.destruction_time <= 0:
                self.destruction_time = time()

