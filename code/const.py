# C
import pygame

COLOR_CYAN_NEON = (0, 255, 255)
COLOR_SHOCKING_PINK = (255, 20, 147)
COLOR_WHITE = (255, 255, 255)
COLOR_ELETRIC_YELLOW = (255, 255, 51)
COLOR_GREEN = (0, 255, 0)
COLOR_RED = (255, 0, 0)

# E

ENTITY_DAMAGE = {
    'Level1Bg01': 0,
    'Level1Bg02': 0,
    'Level1Bg03': 0,
    'Level1Bg04': 0,
    'Level1Bg05': 0,
    'Level1Bg06': 0,
    'PlayerShot': 10,
    'Enemy1Shot': 5,
    'Enemy2Shot': 5,
    'Enemy3Shot': 5,
    'BossShot': 10,
    'Player': 10,
    'Enemy1': 10,
    'Enemy2': 10,
    'Enemy3': 10,
    'Boss': 50,
}

ENTITY_HEALTH = {
    'Level1Bg01': 999,
    'Level1Bg02': 999,
    'Level1Bg03': 999,
    'Level1Bg04': 999,
    'Level1Bg05': 999,
    'Level1Bg06': 999,
    'PlayerShot': 1,
    'Enemy1Shot': 1,
    'Enemy2Shot': 1,
    'Enemy3Shot': 1,
    'BossShot': 1,
    'Player': 50,
    'Enemy1': 20,
    'Enemy2': 20,
    'Enemy3': 20,
    'Boss': 50,
}

ENTITY_SHOT_DELAY = {
    'Player': 30,
    'Enemy1': 150,
    'Enemy2': 150,
    'Enemy3': 150,
    'Boss': 40,
}

ENTITY_SPEED = {
    'Level1Bg01': 0.1,
    'Level1Bg02': 0.2,
    'Level1Bg03': 0.3,
    'Level1Bg04': 0.4,
    'Level1Bg05': 0.5,
    'Level1Bg06': 0.6,
    'Player': 5,
    'Enemy1': 1,
    'Enemy2': 1.2,
    'Enemy3': 1.3,
    'Boss': 1,
    'PlayerShot': 2.5,
    'Enemy1Shot': 2,
    'Enemy2Shot': 2,
    'Enemy3Shot': 2,
    'BossShot': 5,
}

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_BOSS_START = pygame.USEREVENT + 2

# M
MENU_OPTION = ('NEW GAME',
               'EXIT')
# P
PLAYER_KEY_UP = {'Player': pygame.K_UP}
PLAYER_KEY_DOWN = {'Player': pygame.K_DOWN}
PLAYER_KEY_LEFT = {'Player': pygame.K_LEFT}
PLAYER_KEY_RIGHT = {'Player': pygame.K_RIGHT}
PLAYER_KEY_SHOOT = {'Player': pygame.K_SPACE}

# S
SPAWN_TIME_ENEMY = 2000
SPAWN_TIME_BOSS = 2000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
