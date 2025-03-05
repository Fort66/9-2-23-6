from pygame.transform import flip, scale_by
from pygame.image import load

SCALE_VALUE = .225


ENEMY = {
        'angle':{
                0: {
                    'sprite': scale_by(load('images/enemies/1/1.png').convert_alpha(), SCALE_VALUE),
                    'weapons': [[60, 5], [60, -10]]
                    },
                22: {
                    'sprite': scale_by(load('images/enemies/1/2.png').convert_alpha(), SCALE_VALUE),
                    'weapons': [[6, 0], [60, -20]]
                    },
                45: {
                    'sprite': scale_by(load('images/enemies/1/3.png').convert_alpha(), SCALE_VALUE),
                    'weapons': [[60, 5], [60, -25]]
                    },
                67: {
                    'sprite': scale_by(load('images/enemies/1/4.png').convert_alpha(), SCALE_VALUE),
                    'weapons': [[60, 10], [60, -25]]
                    },
                90: {
                    'sprite': scale_by(load('images/enemies/1/5.png').convert_alpha(), SCALE_VALUE),
                    'weapons': [[60, 20], [60, -20]]
                    },
                112: {
                    'sprite': flip(scale_by(load('images/enemies/1/4.png').convert_alpha(), SCALE_VALUE), False, True),
                    'weapons': [[0, 0]]
                    },
                135: {
                    'sprite': flip(scale_by(load('images/enemies/1/3.png').convert_alpha(), SCALE_VALUE), False, True),
                    'weapons': [[0, 0]]
                    },
                157: {
                    'sprite': flip(scale_by(load('images/enemies/1/2.png').convert_alpha(), SCALE_VALUE), False, True),
                    'weapons': [[0, 0]]
                    },
                180: {
                    'sprite': flip(scale_by(load('images/enemies/1/1.png').convert_alpha(), SCALE_VALUE), False, True),
                    'weapons': [[0, 0]]
                    },
                202: {'sprite': flip(scale_by(load('images/enemies/1/2.png').convert_alpha(), SCALE_VALUE), False, True),
                    'weapons': [[0, 0]]
                    },
                225: {
                    'sprite': flip(scale_by(load('images/enemies/1/3.png').convert_alpha(), SCALE_VALUE), False, True),
                    'weapons': [[0, 0]]
                    },
                247: {'sprite': flip(scale_by(load('images/enemies/1/4.png').convert_alpha(), SCALE_VALUE), False, True),
                    'weapons': [[0, 0]]
                    },
                270: {
                    'sprite': flip(scale_by(load('images/enemies/1/5.png').convert_alpha(), SCALE_VALUE), False, True),
                    'weapons': [[0, 0]]
                    },
                292: {
                    'sprite': flip(flip(scale_by(load('images/enemies/1/4.png').convert_alpha(), SCALE_VALUE), False, True), False, True),
                    'weapons': [[0, 0]]
                    },
                315: {
                    'sprite': flip(flip(scale_by(load('images/enemies/1/3.png').convert_alpha(), SCALE_VALUE), False, True), False, True),
                    'weapons': [[0, 0]]
                    },
                337: {
                    'sprite': flip(flip(scale_by(load('images/enemies/1/2.png').convert_alpha(), SCALE_VALUE), False, True), False, True),
                    'weapons': [[0, 0]]
                    },
                359: {
                    'sprite': flip(flip(scale_by(load('images/enemies/1/1.png').convert_alpha(), SCALE_VALUE), False, True), False, True),
                    'weapons': [[0, 0]]
                    },
            },
        'min_distance': 300,
        'shot_distance': 1500,
        'hp': 2,
        'speed': (0, 5),
        'direction_list': [0, 1, -1],
        'move_counter': (0, 6),
        'permission_shot': (1, 3)
    }
