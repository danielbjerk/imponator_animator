import pygame

class Diode():
    def __init__(self, screen_pos, pattern_coord):
        self.screen_pos = screen_pos
        self.pattern_coord = pattern_coord
        self.strength = 0


        self.width = 20
        self.height = 20
        self.x = screen_pos[0]
        self.y = screen_pos[1]

        self.buttonSurface = pygame.Surface((self.width, self.height))
        self.buttonRect = pygame.Rect(self.x, self.y, self.width, self.height)

        font = pygame.font.SysFont('Arial', 40)
        self.buttonSurf = font.render("hello", True, (20, 20, 20))


    def process(self):
        pass


    def draw(self, screen):
        self.buttonSurface.blit(self.buttonSurf, [
            self.buttonRect.width/2 - self.buttonSurf.get_rect().width/2,
            self.buttonRect.height/2 - self.buttonSurf.get_rect().height/2
        ])
        screen.blit(self.buttonSurface, self.buttonRect)
