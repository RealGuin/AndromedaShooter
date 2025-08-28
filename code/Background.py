#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Entity import Entity
from code.const import WIN_WIDTH, ENTITY_SPEED




class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.x = float(self.rect.x)  # posição real

    def move(self, dt: float = 1.0):
        self.x -= ENTITY_SPEED[self.name] * dt
        self.rect.x = int(self.x)
        if self.rect.right <= 0:
            self.x = float(WIN_WIDTH)
            self.rect.left = WIN_WIDTH

#class Background(Entity):
    #def __init__(self, name: str, position: tuple):
       # super().__init__(name, position)


    #def move(self, ):
        #self.rect.centerx -= ENTITY_SPEED[self.name]
        #if self.rect.right <= 0:
            #self.rect.left = WIN_WIDTH