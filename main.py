import pygame as pg
from sys import exit

from loguru import logger

pg.init()


@logger.catch
def main():
    from classes.class_Game import Game

    game = Game()
    game.run_game()


if __name__ == "__main__":
    main()
    pg.quit()
    exit()
