#!/usr/bin/env python3

from src.background import Background, Case
from src.do_game import moves


def cp_line(line) -> list:
    stock_line = []

    for case in line:
        tmp = Case(case.pos_x, case.pos_y, case.size, case.color, case.num)
        stock_line.append(tmp)
    return stock_line


def cp_cases(cases) -> list:
    stock_cases = []

    for case in cases:
        stock_cases.append(cp_line(case))
    return stock_cases


def detect_lose() -> bool:
    print("detect lose\n")
    stock_cases = cp_cases(Background.cases)
    test_moves = moves()

    test_moves.mv_up()
    if test_moves.detect_moves == 1:
        Background.cases.clear()
        Background.cases = cp_cases(stock_cases)
        return False
    test_moves.mv_down()
    if test_moves.detect_moves == 1:
        Background.cases.clear()
        Background.cases = cp_cases(stock_cases)
        return False
    test_moves.mv_left()
    if test_moves.detect_moves == 1:
        Background.cases.clear()
        Background.cases = cp_cases(stock_cases)
        return False
    test_moves.mv_right()
    if test_moves.detect_moves == 1:
        Background.cases.clear()
        Background.cases = cp_cases(stock_cases)
        return False
    print("you lose")
    return True
