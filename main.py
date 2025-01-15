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
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #print(f'Screen width: {SCREEN_WIDTH}')
        #print(f'Screen height: {SCREEN_HEIGHT}')
        screen.fill('black')
        pygame.display.flip()


if __name__ == "__main__":
    main()
