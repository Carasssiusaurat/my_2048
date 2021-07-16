#!/usr/bin/env python3

import sys
import pygame
import time
from src.infos import cases_nb
from src.button import button
from src.my_init_game import init_game

def menu() -> int:
    pygame.init()
    pygame.font.init()
    x, y = 561, 600
    surface = pygame.display.set_mode((x, y))
    back_picture = pygame.image.load("assets/my_2048.png").convert_alpha()
    continu = 1
    left_button = button(50, 300, "assets/left_arrow.png")
    right_button = button(450, 300, "assets/right_arrow.png")
    play_button = button(325, 450, "assets/play_button.png")
    exit_button = button(25, 450, "assets/exit_button.png")
    my_font = pygame.font.SysFont(None, 130)
    text_surface = my_font.render("{0}".format(
        cases_nb.x) + "  *  {0}".format(cases_nb.y), True, [255, 0, 0])
    while continu:
        surface.fill((0, 0, 0))
        surface.blit(back_picture, (0, 0))
        surface.blit(left_button.my_button,
                     (left_button.pos_x, left_button.pos_y))
        surface.blit(right_button.my_button,
                     (right_button.pos_x, right_button.pos_y))
        surface.blit(play_button.my_button,
                     (play_button.pos_x, play_button.pos_y))
        surface.blit(exit_button.my_button,
                     (exit_button.pos_x, exit_button.pos_y))
        surface.blit(text_surface, (175, 300))
        pygame.display.flip()
        if left_button.detect_clic() == True:
            cases_nb.x -= 1
            if cases_nb.x < 3:
                cases_nb.x = 6
            cases_nb.y = cases_nb.x
            text_surface = my_font.render("{0}".format(
                cases_nb.x) + "  *  {0}".format(cases_nb.y), True, [255, 0, 0])
            print("clic on left arrow")
            time.sleep(0.2)
        if right_button.detect_clic() == True:
            cases_nb.x += 1
            if cases_nb.x > 6:
                cases_nb.x = 3
            cases_nb.y = cases_nb.x
            text_surface = my_font.render("{0}".format(
                cases_nb.x) + "  *  {0}".format(cases_nb.y), True, [255, 0, 0])
            print("clic on right arrow")
            time.sleep(0.2)
        if play_button.detect_clic() == True:
            init_game()
            print("clic on play button")
            surface = pygame.display.set_mode((x, y))
            time.sleep(0.2)
        if exit_button.detect_clic() == True:
            print("clic on exit button")
            pygame.quit()
            return 0
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                continu = 0
    pygame.quit()
    return 0