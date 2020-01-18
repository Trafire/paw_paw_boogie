from model.model import map_to_grid
from view import dance_board
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
                    start_x = 50
                    start_y = 50
                    sqaure_size = 100
                    x, y = data


                    if control_map[key]:

                        color = (x* 50,y * 50, 0)
                        pygame.draw.rect(gameDisplay, color, (x * sqaure_size + start_x, y * sqaure_size, sqaure_size, sqaure_size))
                    else:
                        pygame.draw.rect(gameDisplay, black, (x * sqaure_size + start_x, y * sqaure_size, sqaure_size, sqaure_size))

        pygame.display.update()

