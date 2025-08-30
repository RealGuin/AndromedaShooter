#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
from code.Background import Background
from code.Boss import Boss
from code.Enemy import Enemy
from code.Player import Player
from code.const import WIN_WIDTH, WIN_HEIGHT


class EntityFactory:

    @staticmethod
    def get_entity(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Level1Bg':
                list_bg = []
                for i in range(1, 7):  # de 1 até 6
                    list_bg.append(Background(name=f'Level1Bg{i:02d}', position=(0, 0)))
                    list_bg.append(Background(f'Level1Bg{i:02d}', position=(WIN_WIDTH, 0)))
                return list_bg
            case 'Player':
                return Player(entity_name, position=(50, WIN_HEIGHT / 2))
            case 'Enemy1':
                return Enemy(name='Enemy1', position=(WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Enemy2':
                return Enemy(name='Enemy2', position=(WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Enemy3':
                return Enemy(name='Enemy3', position=(WIN_WIDTH + 10, random.randint(50, WIN_HEIGHT - 50)))
            case 'Boss':
                return Boss(name='Boss', position=(WIN_WIDTH + 10, WIN_HEIGHT / 2))
