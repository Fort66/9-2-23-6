from pygame.sprite import (
    groupcollide,
    spritecollideany
)
from time import time
from classes.class_SpriteGroups import SpriteGroups

sprite_groups = SpriteGroups()

def player_guard_collision():
    object_collision = groupcollide(
        sprite_groups.player_guard_group,
        sprite_groups.enemies_shot_group,
        False,
        True
    )

    if object_collision:
        lot_hit = len(list(object_collision.values())[0])
        hits_damage = list(object_collision.values())[0][0].damage
        hit_key = list(object_collision.keys())[0]

        if hit_key.guard_level > 0:
            hit_key.decrease_level(lot_hit * hits_damage)

        if hit_key.guard_level <= 0:
            hit_key.kill()

def enemies_guard_collision():
    object_collision = groupcollide(
        sprite_groups.enemies_guard_group,
        sprite_groups.player_shot_group,
        False,
        True
    )

    if object_collision:
        lot_hit = len(list(object_collision.values())[0])
        hits_damage = list(object_collision.values())[0][0].damage
        hit_key = list(object_collision.keys())[0]

        if hit_key.guard_level > 0:
            hit_key.decrease_level(lot_hit * hits_damage)

        if hit_key.guard_level <= 0:
            hit_key.kill()


def guards_collision():
    object_collision = groupcollide(
        sprite_groups.player_guard_group,
        sprite_groups.enemies_guard_group,
        False,
        False
    )
    if object_collision:
        hit_key = list(object_collision.keys())[0]
        hit_value = list(object_collision.values())[0][0]

        if time() - hit_key.destruction_time >= 1:
            if hit_key.guard_level > 0:
                hit_key.decrease_level(.02)
        if time() - hit_value.destruction_time >= 1:
            if hit_value.guard_level > 0:
                hit_value.decrease_level(.02)

        if hit_key.guard_level <= 0:
            hit_key.kill()
        if hit_value.guard_level <= 0:
            hit_value.kill()

    return object_collision