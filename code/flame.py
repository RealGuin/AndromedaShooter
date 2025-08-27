#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity


class Flame(Entity):
    def __init__(self):
        self.offsetx = None
        self.offsety = None
        self.active = None
        self.frameIndex = None
        self.frameCount = None

    def move(self, ):
        pass

    def setActive(self, on):
        pass
