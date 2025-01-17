#!/bin/python3
#
# the below imports add functionality
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting asteroids!")
    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill('black')
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
