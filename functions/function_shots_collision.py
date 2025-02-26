from pygame.sprite import groupcollide, spritecollideany
from classes.class_SpriteGroups import SpriteGroups
from units.class_Explosion import Explosion

sprite_groups = SpriteGroups()


def player_guard_collision(self):
    if (
        spritecollideany(self, sprite_groups.player_guard_group)
        and self.owner not in sprite_groups.player_group
    ) or (
        spritecollideany(self, sprite_groups.player_group)
        and self.owner not in sprite_groups.player_group
    ):
        explosion = Explosion(
            dir_path="images/explosions/rocket1_expl",
            speed_frames=0.01,
            scale_value=(0.5, 0.5),
            loops=1,
            obj=self,
            angle=self.angle,
        )


def enemies_guard_collision(self):
    if (
        (
        spritecollideany(self, sprite_groups.enemies_guard_group)
        and self.owner not in sprite_groups.enemies_group
        )
        or spritecollideany(self, sprite_groups.enemies_group)
        and self.owner not in sprite_groups.enemies_group
    ):
        explosion = Explosion(
            dir_path="images/explosions/pulsar",
            speed_frames=0.01,
            scale_value=(0.25, 0.25),
            loops=1,
            obj=self,
            angle=self.angle,
        )


def shots_collision(self):
    object_collide = groupcollide(
        sprite_groups.player_shot_group,
        sprite_groups.enemies_shot_group,
        dokilla=True,
        dokillb=False,
    )
    if object_collide:
        hit_value = list(object_collide.values())[0][0]
        explosion = Explosion(
            dir_path="images/explosions/rocket1_expl",
            speed_frames=0.01,
            scale_value=(0.5, 0.5),
            loops=1,
            obj=self,
            angle=self.angle,
        )
        hit_value.kill()
