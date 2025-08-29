#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from code.Entity import Entity
from code.const import ENTITY_SPEED, WIN_HEIGHT, WIN_WIDTH


class Player(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.base_surf = pygame.image.load('./asset/shipPlayer.png').convert_alpha()
        self.flame_surf = pygame.image.load('./asset/shipPlayer_Flame.png').convert_alpha()

    def move(self):
        pressed_key = pygame.key.get_pressed()
        if pressed_key[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_DOWN] and self.rect.bottom < WIN_HEIGHT:
            self.rect.y += ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= ENTITY_SPEED[self.name]
        if pressed_key[pygame.K_RIGHT] and self.rect.right < WIN_WIDTH:
            self.surf = self.flame_surf
            self.rect.x += ENTITY_SPEED[self.name]
        else:
            self.surf = self.base_surf

    def shoot(self):
        pass
