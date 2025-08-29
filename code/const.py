# C
import pygame

COLOR_CYAN_NEON = (0, 255, 255)
COLOR_SHOCKING_PINK = (255, 20, 147)
COLOR_WHITE = (255, 255, 255)
COLOR_ELETRIC_YELLOW = (255, 255, 51)

# E

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_BOSS_START = pygame.USEREVENT + 2

ENTITY_SPEED = {
    'Level1Bg01': 0.1,
    'Level1Bg02': 0.2,
    'Level1Bg03': 0.3,
    'Level1Bg04': 0.4,
    'Level1Bg05': 0.5,
    'Level1Bg06': 0.6,
    'shipPlayer': 5,
    'Enemy1': 1,
    'Enemy2': 1.2,
    'Enemy3': 1.5,
    'Boss':1,
}
# M
MENU_OPTION = ('NEW GAME',
               'EXIT')
# S
SPAWN_TIME_ENEMY = 2000
SPAWN_TIME_BOSS = 60000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

