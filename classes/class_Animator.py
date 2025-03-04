import pygame as pg
from pygame.image import load
from pygame.transform import scale_by

from os import listdir
from time import time

from icecream import ic

import numpy as np
from PIL import Image

from classes.class_SpriteGroups import SpriteGroups


class Animator:
    def __init__(
        self,
        dir_path=None,
        speed_frames=None,
        scale_value=None,
        loops=None,
        size=None,
        no_group=False
    ):
        if not no_group:
            self.sprite_groups = SpriteGroups()
            super().__init__(self.sprite_groups.camera_group)

        self.dir_path = dir_path
        self.speed_frames = speed_frames
        self.size = size
        self.scale_value = scale_value
        self.file_list = listdir(self.dir_path)
        self.file_list.sort(key=lambda x: int(x.split(".")[0]))
        self.image_size = Image.open(f'{self.dir_path}/{self.file_list[0]}').size

        self.frames = None
        self.frame = 0
        self.frame_time = 0
        self.paused = False
        self.loops = loops

        if self.size:
            self.scale_value = (self.size[0] / self.image_size[0] + .05, self.size[1] / self.image_size[1] + .05)
        else:
            self.scale_value = scale_value

        self.__post_init__()

    def __post_init__(self):
        self.original_frames = np.array(
            [
                [
                    scale_by(
                        load(f"{self.dir_path}/{value}").convert_alpha(), self.scale_value
                    ),
                    self.speed_frames,
                ]
                for value in self.file_list
            ]
        )

        self.frames = self.original_frames.copy()
        self.image_rotation = self.frames[self.frame][0]


    def animate(self):
        if self.frame_time == 0:
            self.frame_time = time()

        if time() - self.frame_time >= self.frames[self.frame][1]:
            if self.loops == -1:
                self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else 0
            else:
                if self.loops > 0:
                    self.frame = self.frame + 1 if self.frame < len(self.frames) - 1 else 0
                    if self.frame == len(self.frames) - 1:
                        self.loops -= 1
            self.frame_time = time()

