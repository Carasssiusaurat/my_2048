#!/usr/bin/env python3

import sys, pygame
from random import Random, randint, randrange
from typing import Text
from pygame.constants import K_ESCAPE

class Case:
    cnt_cases = 0

    def __init__(self, my_pos_x, my_pos_y, my_size, my_color) -> None:
        self.pos_x = my_pos_x #int
        self.pos_y = my_pos_y #int
        self.size = my_size #int
        self.color = my_color #tuple, int
        self.num = 0

        Case.cnt_cases += 1

class Background:
    def __init__(self, nb_cases_x, nb_cases_y, height, widht):
        self.cases = []
        pos_y = 10
        y = 0

        while y < nb_cases_y:
            if pos_y > height:
                break
            self.cases.append(self.init_case(pos_y, nb_cases_x, widht))
            pos_y += 97
            y += 1

    def init_case(self, pos_y, nb_cases_x, widht) -> list:
        case = []
        x = 0
        pos_x = 10
        while x < nb_cases_x:
            if pos_x > widht:
                break
            stock = Case(pos_x, pos_y, 87, [255, 0, 0])
            case.append(stock)
            pos_x += 97
            x += 1
        return case

    def draw(self, surface, text) -> None:
        pos = 30
        my_font = pygame.font.SysFont(None, 30)

        for y in self.cases:
            for x in y:
                if x.num != 0:
                    textsurface = my_font.render("{0}".format(x.num), True, x.color)
                    pygame.draw.rect(surface, x.color, pygame.Rect(x.pos_x, x.pos_y, x.size, x.size), 1)
                    surface.blit(textsurface, (x.pos_x + pos, x.pos_y + pos))
                else:
                    pygame.draw.rect(surface, x.color, pygame.Rect(x.pos_x, x.pos_y, x.size, x.size), 1)

def init_inital_nums() -> list:
    case = []
    stock = 0
    case.append(randrange(4))
    case.append(randrange(4))
    stock = randrange(2)
    if stock == 1:
        case.append(2)
    else:
        case.append(4)
    return case

def init_cases_numbers(cases) -> list:
    case_1 = init_inital_nums()
    case_2 = init_inital_nums()

    if case_1[0] == case_2[0] and case_1[1] == case_2[1]:
        init_cases_numbers(cases)
    cases[case_1[0]][case_1[1]].num = case_1[2]
    cases[case_2[0]][case_2[1]].num = case_2[2]
    return cases

def init_game() -> int:
    pygame.init()
    pygame.font.init()
    
    width, height = 400, 400
    surface = pygame.display.set_mode((width,height))
    background = Background(4, 4, height, width)
    text = 10000

    init_cases_numbers(background.cases)
    while 1:
        background.draw(surface, text)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        keys=pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
    return 0