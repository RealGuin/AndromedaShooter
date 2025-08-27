#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

from code.const import WIN_WIDTH, WIN_HEIGHT, COLOR_SHOCKING_PINK, COLOR_CYAN_NEON, MENU_OPTION, COLOR_ELETRIC_YELLOW


class Menu:
    def __init__(self, window):
        self.window = window
        # load the image (convert = faster to draw)
        screenSize = self.surf = pygame.image.load('./asset/MenuBg.png').convert()
        # resize the image to fit the screen size
        self.surf = pygame.transform.scale(screenSize, (WIN_WIDTH, WIN_HEIGHT))
        # resize the image to fit the screen size
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        pygame.mixer_music.load('./asset/Sounds/titleSong.mp3')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            # update the screen
            self.menu_text(text_size=80, text="Ship Wars:", text_color=COLOR_CYAN_NEON,
                           text_center_pos=((WIN_WIDTH / 2), 60))
            self.menu_text(text_size=90, text="Andromeda", text_color=COLOR_ELETRIC_YELLOW,
                           text_center_pos=((WIN_WIDTH / 2), 120))
            for i in range(len(MENU_OPTION)):
                self.menu_text(text_size=60, text=MENU_OPTION[i], text_color=COLOR_SHOCKING_PINK,
                               text_center_pos=((WIN_WIDTH / 2), 250 + 60 * i))

            # draw the background on the window
            pygame.display.flip()

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Window
                    quit()  # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font("./asset/OrbitronFont.ttf", text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
