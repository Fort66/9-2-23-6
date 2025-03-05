from pygame.sprite import Sprite
from pygame.transform import rotozoom

from time import time
from classes.class_Animator import Animator
from functions.function_guards_collision import (
    player_guard_collision,
    enemies_guard_collision,
    guards_collision
    )
from functions.function_load_source import load_json_source

class Guardian(Animator, Sprite):
    def __init__(
        self,
        types=None,
        dir_path=None,
        speed_frames=None,
        guard_level=None,
        scale_value=None,
        loops=None,
        size=None,
        angle=None,
        owner=None
    ):
        if types:
            self.source = load_json_source(
                dir_path="config/sources/guards",
                level=types
            )
            self.dir_path=self.source["dir_path"]
            self.speed_frames=self.source["speed_frames"]
            self.loops = self.source["loops"]
            self.guard_level = self.source["guard_level"]
            self.scale_value = self.source["scale_value"]
        else:
            self.dir_path=dir_path
            self.speed_frames=speed_frames
            self.scale_value=scale_value
            self.loops=loops
            self.guard_level = guard_level

        super().__init__(
            dir_path=self.dir_path,
            speed_frames=self.speed_frames,
            scale_value=self.scale_value,
            loops=self.loops,
            size=size,
        )

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

