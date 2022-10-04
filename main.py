# PyGame template.

# Import standard modules.
import sys

# Import non-standard modules.
import pygame
from pygame.locals import *

import coordinates_to_hex as hx
from patterns.omega import Omega
from patterns.pattern import Pattern
from button import Button


class InteractiveAnimator():
    def __init__(self, pattern : Pattern, save_destination="animation.h"):
        pygame.init()

        #self.last_frame = None#pattern.BLANK_FRAME
        #self.frames = [self.last_frame]

        self.last_pattern = pattern(origin=(50,50), width=300, clickable_diodes=False)
        self.clickable_pattern = pattern(origin=(400,50))

        self.save_button = Button('Lagre og iterér',200,40,(400,450),5,lambda : self.save_and_iterate())
        self.clear_button = Button('Nullstill ramme',200,40,(650,450),5,lambda : self.clickable_pattern.clear_all_diodes())

        self.save_path = save_destination

        # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
        self.fps = 60.0
        self.fpsClock = pygame.time.Clock()

        # Set up the window.
        width, height = 900, 540
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Imponator-Animator')


    def save_hexstring(self):
        hexlist = hx.EMPTY_LIST
        for diode in self.clickable_pattern.diodes:
            hexlist = hx.set_single_pixel(
                hexlist, 
                self.clickable_pattern.pos_to_pattern_coords[diode.pos], 
                diode.strength)
        hexstring = hx.hexlist_to_string(hexlist)

        with open(self.save_path, "a+") as fp:
            fp.write(hexstring + "\n")

    
    def iterate_frames(self):
        last_strength_map = self.clickable_pattern.get_strength_map()
        self.last_pattern.set_strength_map(last_strength_map)
    

    def save_and_iterate(self):
        self.save_hexstring()
        self.iterate_frames()


    def draw(self, screen):
        """
        Draw things to the window. Called once per frame.
        """
        screen.fill('#DCDDD8')

        objects = self.last_pattern.diodes + self.clickable_pattern.diodes + [self.save_button, self.clear_button]
        for obj in objects:
            obj.draw(screen)

        pygame.display.flip()


    def run(self):
        dt = 1/self.fps
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.draw(self.screen)

            dt = self.fpsClock.tick(self.fps)


if __name__ == "__main__":
    ia = InteractiveAnimator(Omega)
    ia.run()
