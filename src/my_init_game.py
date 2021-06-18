#!/usr/bin/env python3

import sys, pygame

def init_game() -> int:
    width, height = 400, 400
    surface = pygame.display.set_mode((width,height))
    color = (255,0,0)
    square_size = 87
    print_square_y = 10
    print_square_x = 10

    pygame.init()
    while 1:
        while print_square_y <= height and print_square_y + square_size + 10 <= height:
            while print_square_x <= width and print_square_x + square_size + 10 <= width:
                pygame.draw.rect(surface, color, pygame.Rect(print_square_x, print_square_y, square_size, square_size), 1)
                print_square_x += square_size + 10
            print_square_x = 10
            print_square_y += square_size + 10
        pygame.display.flip()
        print_square_x = 10
        print_square_y = 10
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit()
    return 0