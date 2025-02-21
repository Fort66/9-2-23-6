from pygame.sprite import Sprite
from classes.class_Animator import Animator


class Guardian(Animator, Sprite):
    def __init__(
        self,
        dir_path=None,
        speed_frames=None,
        obj=None,
        obj_rect=None,
        guard_level=None,
        scale_value=None,
        loops=None,
        pos=None,
    ):

        super().__init__(
            dir_path=dir_path,
            speed_frames=speed_frames,
            obj=obj,
            obj_rect=obj_rect,
            scale_value=scale_value,
            loops=loops,
            pos=pos,
        )

        self.guard_level = guard_level

    @property
    def decrease_level(self):
        if self.guard_level > 0:
            self.guard_level -= 1


    def update(self):
        super().update()