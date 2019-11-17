from model.model import map_to_grid
import pygame


def display(control_map):
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Paw Paw Boogie')
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)
    while True:
        for key in iter(control_map.keys()):

            if type(control_map[key]):

                data = map_to_grid(key)
                if type(data) == tuple:
                    x, y = data
                    x_start = 325
                    y_start = 225
                    if control_map[key]:
                        colour = black

                    else:
                        colour = red
                    pygame.draw.rect(gameDisplay, colour, (x_start + x * 50, y_start * 50, 50, 50))

        pygame.display.update()
