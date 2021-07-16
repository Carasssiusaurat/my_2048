#!/usr/bin/env python3

import sys
import pygame
from pygame.constants import K_ESCAPE
from src.do_game import moves
from src.background import Background, def_new_num
from src.infos import cases_nb

def print_map(cases):
    for x in cases:
        for y in x:
            print(f"{y.num}", end=' ')
        print("")


def calcul_window_size() -> list:
    size = [0, 0]
    nb = 0
    while nb != cases_nb.x:
        size[0] += 97
        nb += 1
    nb = 0
    while nb != cases_nb.y:    
        size[1] += 97
        nb += 1
    size[0] += 10
    size[1] += 10
    return size

def init_game() -> int:
    pygame.init()
    pygame.font.init()

    size = calcul_window_size()
    width, height = size[0], size[1]
    surface = pygame.display.set_mode((width, height))
    background = Background(height, width)

    background.draw(surface)
    pygame.display.flip()
    my_moves = moves()
    print_map(Background.cases)
    if my_moves.detect_moves != 0:
        def_new_num()
    while 1:
        surface.fill((0, 0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            return 0
        if my_moves.get_moves() != 0:
            if my_moves.detect_moves != 0:
                def_new_num()
            print_map(Background.cases)
            background.draw(surface)
            pygame.display.update()

    return 0
