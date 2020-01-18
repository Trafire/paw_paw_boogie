import pygame


class PawSquare:
    def __init__(self, shift, key, control_map, colour, size=50):
        self.surface = pygame.Surface((size, size))
        self.active = False
        location = control_map[key]
        self.key = key
        self.control_map = control_map
        print(control_map)



if __name__ == '__main__':
    gameDisplay = pygame.display.set_mode((800, 600))
    paw = PawSquare((100, 100), (255, 0, 0))

