from pygame.sprite import (
    groupcollide,
    spritecollideany
)
from time import time
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

sprite_groups = SpriteGroups()

def enemies_collision():
    object_collision = groupcollide(
        sprite_groups.enemies_group,
        sprite_groups.player_shot_group,
        False,
        True
    )
    
    if object_collision:
        lot_hits = len(list(object_collision.values())[0])
        hits = list(object_collision.keys())[0]
        
        if hits.hp > 0:
            hits.decrease_hp(lot_hits)
        
        if hits.hp <= 0:
            explosion = Explosion(
                dir_path='images/explosions/ship1_expl',
                speed_frames=0.12,
                scale_value=(.75, .75),
                loops=1,
                obj=hits,
                angle=hits.angle
                )

