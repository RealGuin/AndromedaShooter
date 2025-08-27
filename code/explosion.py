#!/usr/bin/python
# -*- coding: utf-8 -*-

from Entity import Entity


class Explosion(Entity):
    def __init__(self):
        self.frameIndex = None
        self.frameCount = None
        self.frameTimeMs = None
        self.elapsedMs = None
        self.alive = None

    def move(self, ):
        pass
