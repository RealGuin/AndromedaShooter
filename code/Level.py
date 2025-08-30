#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import random
import pygame
from code.Explosion import Explosion
from pygame import Surface, Rect
from pygame.font import Font
from code.Boss import Boss
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player
from code.const import COLOR_WHITE, WIN_HEIGHT, EVENT_ENEMY, EVENT_BOSS_START, SPAWN_TIME_ENEMY, SPAWN_TIME_BOSS, \
    COLOR_RED, COLOR_GREEN, WIN_WIDTH


class Level:
    def __init__(self, window, name, menu_option):
        self.window = window
        self.menu_option = menu_option
        self.name = name
        self.music = True
        self.boss_dead = False
        self.boss_spawned = False
        self.game_over = False
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player'))
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME_ENEMY)
        pygame.time.set_timer(EVENT_BOSS_START, SPAWN_TIME_BOSS, loops=1)
        self.last_boss_pos = (WIN_WIDTH + 10, WIN_HEIGHT / 2)
        self.last_player_pos = (50, WIN_HEIGHT / 2)

    def run(self):

        if self.music:
            pygame.mixer_music.load(f'./asset/soundLevel.mp3')
            pygame.mixer_music.set_volume(0.2)
            pygame.mixer_music.play(-1)

        clock = pygame.time.Clock()

        while True:

            clock.tick(60)  # FPS

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                if ent.name == 'Boss':
                    self.last_boss_pos = ent.rect.center
                if ent.name == 'Player':
                    self.last_player_pos = ent.rect.center
                ent.move()
                if isinstance(ent, (Player, Enemy, Boss)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player':
                    self.level_text(14, f'Player - Health: {ent.health}', COLOR_GREEN, (10, 25))
                if ent.name == 'Boss':
                    self.level_text(14, f'BOSS - Health: {ent.health}', COLOR_RED, (WIN_WIDTH - 200, 25))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        return False
                if event.type == EVENT_ENEMY and not event.type == EVENT_BOSS_START:
                    choice = random.choice(('Enemy1', 'Enemy2', 'Enemy3'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                elif event.type == EVENT_BOSS_START:
                    pygame.time.set_timer(EVENT_ENEMY, 0)
                    self.entity_list.append(EntityFactory.get_entity('Boss'))
                    self.boss_spawned = True
                    self.music = False
                    pygame.mixer_music.load(f'./asset/soundBossBattle.mp3')
                    pygame.mixer_music.set_volume(0.2)
                    pygame.mixer_music.play(-1)

            # Collisions
            EntityMediator.verify_collision(entity_list=self.entity_list)
            EntityMediator.verify_health(entity_list=self.entity_list)
            # Detect Boss death
            if self.boss_spawned and not self.boss_dead and not any(ent.name == 'Boss' for ent in self.entity_list):
                self.boss_dead = True
                self.start_explosion('Boss')
                self.img_the_end = pygame.image.load('./asset/theEnd.png').convert_alpha()
                self.img_the_end = pygame.transform.scale(self.img_the_end, (600, 800))
                self.rect_the_end = self.img_the_end.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))
                for ent in self.entity_list:
                    if ent.name == 'Player':
                        ent.health = 999
            # Detect player death
            if not self.game_over and not any(ent.name == 'Player' for ent in self.entity_list):
                self.game_over = True
                self.start_explosion('Player')
                self.img_game_over = pygame.image.load('./asset/gameOver.png').convert_alpha()
                self.img_game_over = pygame.transform.scale(self.img_game_over, (300, 300))
                self.rect_game_over = self.img_game_over.get_rect(center=(WIN_WIDTH // 2, WIN_HEIGHT // 2))

            # HUD
            self.level_text(14, f'Demo Version 1.0', COLOR_WHITE, (10, 5))
            self.level_text(14, f'FPS: {clock.get_fps():.0f}', COLOR_WHITE, (10, WIN_HEIGHT - 35))
            #self.level_text(14, f'Entidades: {len(self.entity_list)}', COLOR_WHITE, (10, WIN_HEIGHT - 20))

            if self.boss_dead:
                self.window.blit(self.img_the_end, self.rect_the_end)
            if self.game_over:
                self.window.blit(self.img_game_over, self.rect_game_over)

            pygame.display.flip()

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/OrbitronFont.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)

    def start_explosion(self, name: str):

        explosion = Explosion(self.window)

        if name == 'Boss':
            explosion.explosion_Boss(self.last_boss_pos)
        elif name == 'Player':
            explosion.explosion_Player(self.last_player_pos)