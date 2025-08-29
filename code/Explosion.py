#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame



import pygame


class Explosion:
    def __init__(self, window: pygame.Surface):
        self.window = window

    def explosion_Boss(self, pos: tuple):
        frames = [pygame.image.load(f'./asset/Explosion1_{i:02d}.png').convert_alpha() for i in range(1, 12)]
        sound = pygame.mixer.Sound('./asset/soundDeath.mp3')
        sound.set_volume(0.2)
        sound.play()

        clock = pygame.time.Clock()
        for frame in frames:
            self.window.fill((0, 0, 0))
            self.window.blit(frame, frame.get_rect(center=pos))
            pygame.display.flip()
            clock.tick(10)

        pygame.mixer.music.load('./asset/soundTheEnd.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)

    def explosion_Player(self, pos: tuple):
        frames = [pygame.image.load(f'./asset/Explosion1_{i:02d}.png').convert_alpha() for i in range(1, 12)]
        sound = pygame.mixer.Sound('./asset/soundDeath.mp3')
        sound.set_volume(0.2)
        sound.play()

        clock = pygame.time.Clock()
        for frame in frames:
            self.window.fill((0, 0, 0))
            self.window.blit(frame, frame.get_rect(center=pos))
            pygame.display.flip()
            clock.tick(20)

        pygame.mixer.music.load('./asset/soundGameOver.mp3')
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
