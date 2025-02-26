from pygame.sprite import Sprite
from pygame.transform import rotozoom

from time import time
from classes.class_Animator import Animator



class Explosion(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frames=None,
        obj=None,
        scale_value=None,
        loops=None,
        size=None,
        angle=None
    ):

        super().__init__(
            dir_path=dir_path,
            speed_frames=speed_frames,
            scale_value=scale_value,
            loops=loops,
            size=size,
        )

        self.obj = obj
        self.angle = angle
        self.rect = self.image_rotation.get_rect(center=self.obj.rect.center)

    def update(self):
        if self.loops > 0:
            self.angle = self.obj.angle
            self.image_rotation = self.frames[self.frame][0]
            self.image_rotation = rotozoom(self.image_rotation, self.angle, 1)
            self.rect = self.image_rotation.get_rect(center=self.rect.center)
            super().animate()
        else:
            self.kill()