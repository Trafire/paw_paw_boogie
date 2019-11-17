from model.model import map_to_grid
import pygame

def display(control_map):
    gameDisplay = pygame.display.set_mode((800,600))
    pygame.display.set_caption('Paw Paw Boogie')
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    for key in control_map:
        print(key)
        if control_map[key]:
            x,y = map_to_grid(key)
            pygame.draw.rect(gameDisplay, blue, pygame.Rect(x*50,y*50, 50))
