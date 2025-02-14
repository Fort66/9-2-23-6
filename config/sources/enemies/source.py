from pygame.transform import flip, scale_by
from pygame.image import load

SCALE_VALUE = {
                1: .25,
               }


ENEMIES = {
            1:
                {'angle':{
                            0: {
                                'sprite': scale_by(load('images/Ships/Spaceship16/ship1.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[60, 5], [60, -10]]
                                },
                            22: {
                                'sprite': scale_by(load('images/Ships/Spaceship16/ship2.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[6, 0], [60, -20]]
                                },
                            45: {
                                'sprite': scale_by(load('images/Ships/Spaceship16/ship3.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[60, 5], [60, -25]]
                                },
                            67: {
                                'sprite': scale_by(load('images/Ships/Spaceship16/ship4.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[60, 10], [60, -25]]
                                },
                            90: {
                                'sprite': scale_by(load('images/Ships/Spaceship16/ship5.png').convert_alpha(), SCALE_VALUE[1]),
                                'weapons': [[60, 20], [60, -20]]
                                },
                            112: {
                                'sprite': flip(scale_by(load('images/Ships/Spaceship16/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[0, 0]]
                                },
                            135: {
                                'sprite': flip(scale_by(load('images/Ships/Spaceship16/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[0, 0]]
                                },
                            157: {
                                'sprite': flip(scale_by(load('images/Ships/Spaceship16/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[0, 0]]
                                },
                            180: {
                                'sprite': flip(scale_by(load('images/Ships/Spaceship16/ship1.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[0, 0]]
                                },
                            202: {'sprite': flip(scale_by(load('images/Ships/Spaceship16/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[0, 0]]
                                },
                            225: {
                                'sprite': flip(scale_by(load('images/Ships/Spaceship16/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[0, 0]]
                                },
                            247: {'sprite': flip(scale_by(load('images/Ships/Spaceship16/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[0, 0]]
                                },
                            270: {
                                'sprite': flip(scale_by(load('images/Ships/Spaceship16/ship5.png').convert_alpha(), SCALE_VALUE[1]), False, True),
                                'weapons': [[0, 0]]
                                },
                            292: {
                                'sprite': flip(flip(scale_by(load('images/Ships/Spaceship16/ship4.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
                                'weapons': [[0, 0]]
                                },
                            315: {
                                'sprite': flip(flip(scale_by(load('images/Ships/Spaceship16/ship3.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
                                'weapons': [[0, 0]]
                                },
                            337: {
                                'sprite': flip(flip(scale_by(load('images/Ships/Spaceship16/ship2.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
                                'weapons': [[0, 0]]
                                },
                            359: {
                                'sprite': flip(flip(scale_by(load('images/Ships/Spaceship16/ship1.png').convert_alpha(), SCALE_VALUE[1]), False, True), False, True),
                                'weapons': [[0, 0]]
                                },
                        },
                }
        }