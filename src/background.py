#!/usr/bin/env python3

import sys
import pygame
from random import randrange
from src.infos import cases_nb

class Case:
    cnt_cases = 0

    def __init__(self, my_pos_x: int, my_pos_y: int, my_size: int, my_color: tuple, my_num: int) -> None:
        self.pos_x = my_pos_x  # int
        self.pos_y = my_pos_y  # int
        self.size = my_size  # int
        self.color = my_color  # tuple, int
        self.num = my_num

        Case.cnt_cases += 1


class Background:

    cases = []

    def __init__(self, height: int, widht: int):
        pos_y = 10
        y = 0

        while y < cases_nb.y:
            if pos_y > height:
                break
            self.cases.append(self.init_case(pos_y, widht))
            pos_y += 97
            y += 1
        self.init_cases_numbers()

    def init_case(self, pos_y: int, widht: int) -> list:
        case = []
        x = 0
        pos_x = 10

        while x < cases_nb.x:
            if pos_x > widht:
                break
            stock = Case(pos_x, pos_y, 87, [255, 0, 0], 0)
            case.append(stock)
            pos_x += 97
            x += 1
        return case

    def init_inital_nums(self) -> list:
        case = []
        stock = 0

        case.append(randrange(cases_nb.x))
        case.append(randrange(cases_nb.y))
        stock = randrange(2)
        if stock == 1:
            case.append(2)
        else:
            case.append(4)
        return case

    def init_cases_numbers(self):
        case_1 = self.init_inital_nums()
        case_2 = self.init_inital_nums()

        print(f"case_1 x = {case_1[0]} case_1 y = {case_1[1]}")
        print(f"case_2 x = {case_2[0]} case_2 y = {case_2[1]}\n")

        if case_1[0] == case_2[0] and case_1[1] == case_2[1]:
            self.init_cases_numbers()
        self.cases[case_1[1]][case_1[0]].num = case_1[2]
        self.cases[case_2[1]][case_2[0]].num = case_2[2]

    def draw(self, surface) -> None:
        pos = 30
        my_font = pygame.font.SysFont(None, 30)

        for y in self.cases:
            for x in y:
                if x.num != 0:
                    textsurface = my_font.render(
                        "{0}".format(x.num), True, x.color)
                    pygame.draw.rect(surface, x.color, pygame.Rect(
                        x.pos_x, x.pos_y, x.size, x.size), 1)
                    surface.blit(textsurface, (x.pos_x + pos, x.pos_y + pos))
                else:
                    pygame.draw.rect(surface, x.color, pygame.Rect(
                        x.pos_x, x.pos_y, x.size, x.size), 1)

def init_new_num() -> list:
    case = []
    case.append(randrange(cases_nb.x))
    case.append(randrange(cases_nb.y))
    if randrange(2) == 1:
        case.append(2)
    else:
        case.append(4)
    return case

def def_new_num() -> None:
    case = init_new_num()

    while Background.cases[case[0]][case[1]].num != 0:
        case = init_new_num()
    Background.cases[case[0]][case[1]].num = case[2]