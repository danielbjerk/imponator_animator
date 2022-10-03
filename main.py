# PyGame template.

# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *

from patterns import omega


class InteractiveAnimator():
    def __init__(self, pattern, save_destination="animation.h"):
        pygame.init()

        self.last_frame = None#pattern.BLANK_FRAME
        self.frames = [self.last_frame]

        self.objects = pattern.diodes #+ [save+next-button og clear-button]

        self.save_path = save_destination


        # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
        self.fps = 60.0
        self.fpsClock = pygame.time.Clock()

        # Set up the window.
        width, height = 640, 480
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Imponator-Animator')
        # screen is the surface representing the window.
        # PyGame surfaces can be thought of as screen sections that you can draw onto.
        # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.


    def save_hexstring(self):
        hexlist = hx.EMPTY_LIST
        for diode in self.objects:
            hexlist = hx.update_hexlist(hexlist, diode.hex_coords, diode.strength)
        hexstring = hx.list_to_string(hexlist)

        with open(self.save_path) as fp:
            fp.writelines(hexstring)


    def draw(self, screen):
        """
        Draw things to the window. Called once per frame.
        """
        screen.fill('#DCDDD8')

        # Redraw screen here.
        for obj in self.objects:
            obj.draw(screen)

        # Flip the display so that the things we drew actually show up.
        #pygame.display.flip()
        pygame.display.update()


    def run(self):
        dt = 1/self.fps # dt is the time since last frame.
        while True: # Loop forever!
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw(self.screen)

            dt = self.fpsClock.tick(self.fps)


if __name__ == "__main__":
    ia = InteractiveAnimator(omega.Omega())
    ia.run()

