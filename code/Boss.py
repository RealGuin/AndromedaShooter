#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import pygame
from code.BossShot import BossShot
from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, ENTITY_SHOT_DELAY


class Boss(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.spawn_time = pygame.time.get_ticks()
        self.active_speed = ENTITY_SPEED[self.name]
        self.stopped = False
        self.dir_y = 0

    def move(self):
        # fixed vertical speed
        self.rect.y += self.dir_y * 2

        if not self.stopped and pygame.time.get_ticks() - self.spawn_time >= 3000:
            self.active_speed = 0
            self.stopped = True
            self.dir_y = random.choice([-1, 1])

        self.rect.centerx -= self.active_speed

        # screen limits
        if self.rect.top <= 0:
            self.rect.top = 0
            self.dir_y = 1
        elif self.rect.bottom >= WIN_HEIGHT:
            self.rect.bottom = WIN_HEIGHT
            self.dir_y = -1
        # Random chance to switch in the middle.
        if random.random() < 0.01:
            self.dir_y *= -1

    def shoot(self, ):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            sound = pygame.mixer.Sound('./asset/soundShot02.mp3')
            sound.set_volume(0.1)
            sound.play()
            return BossShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))