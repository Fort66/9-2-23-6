from pygame.sprite import (
    groupcollide,
    spritecollideany
)
from time import time
from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def enemies_collision():
    object_collision = groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        False,
        True
    )