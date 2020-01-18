from model.model import map_to_grid
from view import dance_board
import pygame
from view.paw_print import Paw

def display(control_map):
    gameDisplay = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Paw Paw Boogie')
    black = (0, 0, 0)
    blue = (0, 0, 255)
    red = (255, 0, 0)

    start_x = 50
    start_y = 50
    sqaure_size = 100
    done = {black:Paw(black, sqaure_size)}
    while True:
        for key in iter(control_map.keys()):
            if type(control_map[key]):
                data = map_to_grid(key)
                if type(data) == tuple:

                    x, y = data
                    color = (x * 50, y * 50, 0)
                    if color not in done:
                        p = Paw(color, sqaure_size)
                        done[color] = p

                    if control_map[key]:
                        image = done[color].get_image()
                        gameDisplay.blit(image.get_image(), (a.width, 0))
                        #pygame.draw.rect(gameDisplay, color, (x * sqaure_size + start_x, y * sqaure_size, sqaure_size, sqaure_size))

                    else:
                        image = done[color]
                        gameDisplay.blit(image.get_image(), (image.width, 0))
                        pygame.draw.rect(gameDisplay, black, (x * sqaure_size + start_x, y * sqaure_size, sqaure_size, sqaure_size))
        pygame.display.update()
