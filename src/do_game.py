#!/usr/bin/env python3

import sys
import pygame
import time
from pygame.constants import K_DOWN, K_LEFT, K_RIGHT, K_UP
from pygame.sprite import OrderedUpdates
from src.background import Background
from src.infos import cases_nb


class moves:

    detect_moves = 0

    def get_moves(self) -> int:
        key = pygame.key.get_pressed()

        self.detect_moves = 0
        if key[K_UP]:
            self.mv_up()
            time.sleep(0.2)
            return 1
        if key[K_RIGHT]:
            self.mv_right()
            time.sleep(0.2)
            return 1
        if key[K_DOWN]:
            self.mv_down()
            time.sleep(0.2)
            return 1
        if key[K_LEFT]:
            self.mv_left()
            time.sleep(0.2)
            return 1
        return 0

    def mv_up(self) -> None:
        x, y, o_y, my_len = 0, 0, 0, 0

        print("mv_up")
        while x < cases_nb.x:
            while y < cases_nb.y:
                my_len = len(Background.cases[y])
                if y < cases_nb.y - 1 and Background.cases[y + 1][x].num == 0:
                    o_y = y + 1
                    while o_y < cases_nb.y - 1 and Background.cases[o_y][x].num == 0:
                        o_y += 1
                    if Background.cases[o_y][x].num != 0 and Background.cases[o_y][x].num == Background.cases[y][x].num:
                        Background.cases[y][x].num += Background.cases[o_y][x].num
                        Background.cases[o_y][x].num = 0
                        self.detect_moves = 1
                if y + 1 != my_len and Background.cases[y][x].num == Background.cases[y + 1][x].num:
                    Background.cases[y][x].num += Background.cases[y + 1][x].num
                    Background.cases[y + 1][x].num = 0
                    self.detect_moves = 1
                y += 1
            x += 1
            y = 0
        self.do_classic_mv_up()

    def do_classic_mv_up(self) -> None:
        x, y, o_y = 0, 0, 0

        while x < cases_nb.x:
            while y < cases_nb.y - 1:
                if Background.cases[y][x].num == 0:
                    o_y = y
                    while o_y < cases_nb.y - 1 and Background.cases[o_y][x].num == 0:
                        o_y += 1
                    if Background.cases[o_y][x].num != 0:
                        Background.cases[y][x].num = Background.cases[o_y][x].num
                        Background.cases[o_y][x].num = 0
                        self.detect_moves = 1
                y += 1
            x += 1
            y = 0

    def mv_down(self) -> None:
        x, y, o_y, my_len = cases_nb.x - 1, cases_nb.y - 1, 0, 0

        print("mv_down")
        while x >= 0:
            while y > 0:
                my_len = len(Background.cases[y])
                if y > 0 and Background.cases[y - 1][x].num == 0:
                    o_y = y - 1
                    while o_y > 0 and Background.cases[o_y][x].num == 0:
                        o_y -= 1
                    if Background.cases[o_y][x].num != 0 and Background.cases[o_y][x].num == Background.cases[y][x].num:
                        Background.cases[y][x].num += Background.cases[o_y][x].num
                        Background.cases[o_y][x].num = 0
                        self.detect_moves = 1
                if Background.cases[y][x].num == Background.cases[y - 1][x].num:
                    Background.cases[y][x].num += Background.cases[y - 1][x].num
                    Background.cases[y - 1][x].num = 0
                    self.detect_moves = 1
                y -= 1
            x -= 1
            y = cases_nb.y - 1
        self.do_classic_mv_down()

    def do_classic_mv_down(self) -> None:
        x, y, o_y = cases_nb.x - 1, cases_nb.y - 1, 0

        while x >= 0:
            while y > 0:
                if Background.cases[y][x].num == 0:
                    o_y = y
                    while o_y > 0 and Background.cases[o_y][x].num == 0:
                        o_y -= 1
                    if Background.cases[o_y][x].num != 0:
                        Background.cases[y][x].num = Background.cases[o_y][x].num
                        Background.cases[o_y][x].num = 0
                        self.detect_moves = 1
                y -= 1
            x -= 1
            y = cases_nb.y - 1

    def mv_left(self) -> None:
        x, y, o_x = 0, 0, 0

        print("mv_left")
        while y < cases_nb.y:
            while x < cases_nb.x - 1:
                if x < cases_nb.x - 1 and Background.cases[y][x + 1].num == 0:
                    o_x = x + 1
                    while o_x < cases_nb.x - 1 and Background.cases[y][o_x].num == 0:
                        o_x += 1
                    if Background.cases[y][x].num == Background.cases[y][o_x].num:
                        Background.cases[y][x].num += Background.cases[y][o_x].num
                        Background.cases[y][o_x].num = 0
                        self.detect_moves = 1
                if x + 1 < cases_nb.x and Background.cases[y][x].num == Background.cases[y][x + 1].num:
                    Background.cases[y][x].num += Background.cases[y][x + 1].num
                    Background.cases[y][x + 1].num = 0
                    self.detect_moves = 1
                x += 1
            y += 1
            x = 0
        self.do_classic_mv_left()

    def do_classic_mv_left(self) -> None:
        x, y, o_x = 0, 0, 0

        while y < cases_nb.y:
            while x < cases_nb.y - 1:
                if Background.cases[y][x].num == 0:
                    o_x = x
                    while o_x < cases_nb.x - 1 and Background.cases[y][o_x].num == 0:
                        o_x += 1
                    if Background.cases[y][o_x].num != 0:
                        Background.cases[y][x].num = Background.cases[y][o_x].num
                        Background.cases[y][o_x].num = 0
                        self.detect_moves = 1
                x += 1
            y += 1
            x = 0

    def mv_right(self) -> None:
        x, y, o_x, my_len = cases_nb.x - 1, 0, 0, 0

        print("mv_right")
        while y <= cases_nb.x - 1:
            while x > 0:
                my_len = len(Background.cases[y])
                if x > 0 and Background.cases[y][x - 1].num == 0:
                    o_x = x - 1
                    while o_x > 0 and Background.cases[y][o_x].num == 0:
                        o_x -= 1
                    if Background.cases[y][x].num == Background.cases[y][o_x].num:
                        Background.cases[y][x].num += Background.cases[y][o_x].num
                        Background.cases[y][o_x].num = 0
                        self.detect_moves = 1
                if Background.cases[y][x].num == Background.cases[y][x - 1].num:
                    Background.cases[y][x].num += Background.cases[y][x - 1].num
                    Background.cases[y][x - 1].num = 0
                    self.detect_moves = 1
                x -= 1
            y += 1
            x = cases_nb.x - 1
            self.do_classic_mv_right()

    def do_classic_mv_right(self) -> None:
        x, y, o_x = cases_nb.x - 1, cases_nb.y - 1, 0

        while y >= 0:
            while x != 0:
                if Background.cases[y][x].num == 0:
                    o_x = x
                    while o_x != 0 and Background.cases[y][o_x].num == 0:
                        o_x -= 1
                    if Background.cases[y][o_x].num != 0:
                        Background.cases[y][x].num = Background.cases[y][o_x].num
                        Background.cases[y][o_x].num = 0
                        self.detect_moves = 1
                x -= 1
            y -= 1
            x = cases_nb.x - 1
