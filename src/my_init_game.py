#!/usr/bin/env python3

import sys
import pygame
from typing import Text
from pygame.constants import K_ESCAPE
from src.do_game import moves
from src.background import Background, def_new_num


def print_map(cases):
    print(
        f"{cases[0][0].num} {cases[0][1].num} {cases[0][2].num} {cases[0][3].num}")
    print(
        f"{cases[1][0].num} {cases[1][1].num} {cases[1][2].num} {cases[1][3].num}")
    print(
        f"{cases[2][0].num} {cases[2][1].num} {cases[2][2].num} {cases[2][3].num}")
    print(
        f"{cases[3][0].num} {cases[3][1].num} {cases[3][2].num} {cases[3][3].num}\n")


def init_game() -> int:
    pygame.init()
    pygame.font.init()

    width, height = 400, 400
    surface = pygame.display.set_mode((width, height))
    background = Background(height, width)

    background.draw(surface)
    pygame.display.flip()
    my_moves = moves()
    def_new_num()
    while 1:
        surface.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        if my_moves.get_moves() != 0:
            print_map(Background.cases)
            background.draw(surface)
            pygame.display.update()
            def_new_num()

    return 0
