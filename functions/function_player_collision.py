from pygame.sprite import (
    groupcollide,
    spritecollideany
)
from time import time
from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def player_collision():
    object_collision = groupcollide(
        sprite_groups.player_group,
        sprite_groups.enemies_shot_group,
        False,
        True
    )