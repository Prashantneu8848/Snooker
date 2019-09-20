import pygame

def border(display, wood, width, height):
    pygame.draw.rect(display, wood, (0, 0, width, 30))
    pygame.draw.rect(display, wood, (0, 0, 30, height))
    pygame.draw.rect(display, wood, (width - 30, 0, width, height))
    pygame.draw.rect(display, wood, (0, height - 30, width, height))