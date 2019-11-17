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
                    x += 325
                    y += 225
                    if control_map[key]:
                        pygame.draw.rect(gameDisplay, red, (x * 50, y * 50, 50, 50))
                    else:
                        pygame.draw.rect(gameDisplay, black, (x * 50, y * 50, 50, 50))

        pygame.display.update()
