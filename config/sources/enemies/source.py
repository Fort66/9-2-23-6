from pygame.transform import flip, scale_by
from pygame.image import load


SCALE_VALUE = {
                1: .25
                }

ENEMIES = {
            0: scale_by(load('images/enemies/spaceship1/ship1.png').convert_alpha(), SCALE_VALUE[1]),
            22: scale_by(load('images/enemies/spaceship1/ship2.png').convert_alpha(), SCALE_VALUE[1]),
            45: scale_by(load('images/enemies/spaceship1/ship3.png').convert_alpha(), SCALE_VALUE[1]),
            67: scale_by(load('images/enemies/spaceship1/ship4.png').convert_alpha(), SCALE_VALUE[1]),
            90: scale_by(load('images/enemies/spaceship1/ship5.png').convert_alpha(), SCALE_VALUE[1]),
            112: flip(scale_by(load('images/enemies/spaceship1/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True),
            135: flip(scale_by(load('images/enemies/spaceship1/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True),
            157: flip(scale_by(load('images/enemies/spaceship1/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True),
            180: flip(scale_by(load('images/enemies/spaceship1/ship1.png').convert_alpha(), SCALE_VALUE[1]), False, True),
            202: flip(scale_by(load('images/enemies/spaceship1/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True),
            225: flip(scale_by(load('images/enemies/spaceship1/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True),
            247: flip(scale_by(load('images/enemies/spaceship1/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True),
            270: flip(scale_by(load('images/enemies/spaceship1/ship5.png').convert_alpha(), SCALE_VALUE[1]), False, True),
            292: flip(flip(scale_by(load('images/enemies/spaceship1/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
            315: flip(flip(scale_by(load('images/enemies/spaceship1/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
            337: flip(flip(scale_by(load('images/enemies/spaceship1/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
            359: flip(flip(scale_by(load('images/enemies/spaceship1/ship1.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
            }