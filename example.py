###
### Source: https://github.com/clear-code-projects/elevatedButton
###

import pygame, sys

class Button:
    def __init__(self,radius,pos):
		#Core attributes
        elevation = 5	# Previously an argument
        self.pressed = False
        self.radius = radius
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

		# Diode strength
        self.strength = 0
        self.strength_to_color = [(0,0,0)] + [(255 - 13*i, 0, 0) for i in range(15)]

		# top rectangle
        self.top_rect = pygame.Rect(pos,(radius,radius))
        self.top_color = self.strength_to_color[self.strength]

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(radius,radius))
        self.bottom_color = '#354B5E'

        # text
        self.font = pygame.font.Font(None,30)
        self.text_surf = self.font.render(str(self.strength),True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)


    def draw(self):
        self.handle_click()

		# elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elecation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elecation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = self.radius//2)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = self.radius//2)
        screen.blit(self.text_surf, self.text_rect)
		#self.handle_click()


    def handle_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elecation = 0
                self.pressed = True
            else:
                self.dynamic_elecation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    self.strength = (self.strength + 1) % 16
        else:
            self.dynamic_elecation = self.elevation
        self.top_color = self.strength_to_color[self.strength]
        self.text_surf = self.font.render(str(self.strength),True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)


    def reset_strength(self):
        self.strength = 0



pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption('Gui Menu')
clock = pygame.time.Clock()

button1 = Button(40,(200,250))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('#DCDDD8')
    button1.draw()

    pygame.display.update()
    clock.tick(60)
