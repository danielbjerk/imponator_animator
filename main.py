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


    def update(self, dt):
        """
        Update game. Called once per frame.
        dt is the amount of time passed since last frame.
        If you want to have constant apparent movement no matter your framerate,
        what you can do is something like
        
        x += v * dt
        
        and this will scale your velocity based on time. Extend as necessary."""
        
        # Go through events that are passed to the script by the window.
        for event in pygame.event.get():
        # We need to handle these events. Initially the only one you'll want to care
        # about is the QUIT event, because if you don't handle it, your game will crash
        # whenever someone tries to exit.
            if event.type == QUIT:
                pygame.quit() # Opposite of pygame.init
                sys.exit() # Not including this line crashes the script on Windows. Possibly
                # on other operating systems too, but I don't know for sure.
            # Handle other events as you wish.

        for obj in self.objects:
            obj.process()


        # Check if "save and go to next frame" or "clear current frame" is pressed here
        

    def draw(self, screen):
        """
        Draw things to the window. Called once per frame.
        """
        screen.fill((0, 0, 0)) # Fill the screen with black.
        
        # Redraw screen here.
        for obj in self.objects:
            obj.draw(screen)
        
        # Flip the display so that the things we drew actually show up.
        pygame.display.flip()


    def run(self):
        dt = 1/self.fps # dt is the time since last frame.
        while True: # Loop forever!
            self.update(dt) # You can update/draw here, I've just moved the code for neatness.
            self.draw(self.screen)
            
            dt = self.fpsClock.tick(self.fps)


if __name__ == "__main__":
    ia = InteractiveAnimator(omega.Omega())
    ia.run()

