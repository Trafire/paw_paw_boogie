import cv2
import pygame
import webcolors


class Paw:
    def __init__(self, colour, height=None, width=None, text = "unknown"):
        '''
        :param colour: (int,int,int) - tuple of three ints between 0 and 255

        '''

        base_filename = "view/images/paw_print/pawprint.png"
        self.image = cv2.imread(base_filename)
        self.change_colour(colour)
        self._get_dimensions()
        if height or width:
            self.resize(width, height)
        self.create_desaturated()
        self.save()

    def change_colour(self, colour):
        self.colour = colour
        print(self.image)
        Conv_hsv_Gray = cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)
        ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
        print("Colour: ", colour)
        self.image[mask == 255] = colour[::-1]

    def create_desaturated(self):
        self.image_desaturated = cv2.convertScaleAbs(self.image, alpha=.2,beta=0.5)


    def _get_dimensions(self):
        self.height, self.width, channels = self.image.shape
        return (self.width, self.height)

    def get_filename(self, desaturated=False):
        self._get_dimensions()
        self.filename = "view/images/paw_print/colour/paw-{}-{}-{}-{}x{}.jpg".format(self.colour[0], self.colour[1], self.colour[2], self.height, self.width)
        self.filename_desaturated = "view/images/paw_print/colour/desaturated_paw-{}-{}-{}-{}x{}.jpg".format(self.colour[0], self.colour[1], self.colour[2], self.height, self.width)
        return self.filename

    def save(self):
        self.get_filename()
        cv2.imwrite(self.filename, self.image)
        cv2.imwrite(self.filename_desaturated, self.image_desaturated)


    def _show(self):
        cv2.imshow('', self.image)
        cv2.waitKey(0)

    def get_image(self, selected = False):
        if not selected:
            return pygame.image.load(self.filename_desaturated)
        return pygame.image.load(self.filename)

    def resize(self, width=None, height=None):
        width_ratio, height_ratio = None, None
        if width:
            width_ratio = width / self.width
            ratio = width_ratio
        if height:
            height_ratio = height / self.height
            ratio = height_ratio
        if height_ratio and width_ratio:
            ratio = min(width_ratio, height_ratio)
        new_width = self.width * ratio
        new_height = self.height * ratio
        dsize = (int(new_width), int(new_height))
        output = cv2.resize(self.image, dsize)
        self.height, self.width, channels = output.shape
        self.image = output

    def get_colour_name(self):
        print(tuple(self.colour))
        return webcolors.rgb_to_name(tuple(self.colour))


if __name__ == "__main__":
    HEIGHT_RATIO = .2
    pygame.init()
    screen_width = int(pygame.display.Info().current_w * .75)
    screen_height = int(pygame.display.Info().current_h * .75)
    target_height = int(screen_height * HEIGHT_RATIO)

    a = Paw([0, 0, 255], height=target_height)
    b = Paw([255, 0, 0], height=target_height)
    c = Paw([0, 255, 0], height=target_height)
    # c.resize(width=100)
    # c.resize(width=1000)


    display = (screen_width, screen_height)
    display_surface = pygame.display.set_mode(display,pygame.RESIZABLE)
    #pygame.display.toggle_fullscreen()
    white = [0, 0, 0]
    while True:
        image = a.get_image()

        # completely fill the surface object
        # with white colour
        display_surface.fill(white)

        # copying the image surface object
        # to the display surface object at
        # (0, 0) coordinate.
        display_surface.blit(a.get_image(), (0, 0))
        display_surface.blit(b.get_image(), (a.width, 0))

        # iterate over the list of Event objects
        # that was returned by pygame.event.get() method.
        for event in pygame.event.get():

            # if event object type is QUIT
            # then quitting the pygame
            # and program both.
            if event.type == pygame.QUIT:
                # deactivates the pygame library
                pygame.quit()

                # quit the program.
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.display.toggle_fullscreen()

                # Draws the surface object to the screen.
            pygame.display.update()
