#!/usr/bin/env python3

import pygame


class button:
    def __init__(self, x, y, picture):
        self.pos_x, self.pos_y = x, y
        self.my_button = pygame.image.load(picture).convert_alpha()
        self.my_button_rect = self.my_button.get_rect(topleft=(x, y))

    def detect_clic(self) -> bool:
        if pygame.mouse.get_focused():
            x, y = pygame.mouse.get_pos()
            collide = self.my_button_rect.collidepoint(x, y)
            pressed = pygame.mouse.get_pressed()
            if collide and pressed[0]:
                return True
        else:
            return False