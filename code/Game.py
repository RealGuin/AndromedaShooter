#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import pygame
from code.Level import Level
from code.Menu import Menu
from code.const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                level = Level(self.window, name='Level1bg', menu_option=menu_return)
                level.run()
            else:
                pygame.quit()
                sys.exit()
