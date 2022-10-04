###
### Source: https://github.com/clear-code-projects/elevatedButton
###

import pygame, sys

class Diode:
    def __init__(self,radius,pos,colors,clickable):
		#Core attributes
        pygame.init()   # Unsafe?
        self.pos = pos
        elevation = 5	# Previously an argument
        self.pressed = False
        self.radius = radius
        self.elevation = elevation
        self.dynamic_elevation = elevation
        self.original_y_pos = pos[1]

		# Diode strength
        self.strength_to_color = colors
        self.strength = 0
        self.max_strength = len(colors)

		# top rectangle
        self.top_rect = pygame.Rect(pos,(radius,radius))
        self.top_color = self.strength_to_color[self.strength]

        # bottom rectangle
        self.bottom_rect = pygame.Rect(pos,(radius,radius))
        self.bottom_color = '#354B5E'

        # text
        self.font = pygame.font.Font(None,int(30*(radius/40)))
        self.text_surf = self.font.render(str(self.strength),True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)

        self.clickable = clickable


    def draw(self, screen):
        if self.clickable: self.handle_click()

		# elevation logic
        self.top_rect.y = self.original_y_pos - self.dynamic_elevation
        self.text_rect.center = self.top_rect.center

        self.bottom_rect.midtop = self.top_rect.midtop
        self.bottom_rect.height = self.top_rect.height + self.dynamic_elevation

        pygame.draw.rect(screen,self.bottom_color, self.bottom_rect,border_radius = self.radius//2)
        pygame.draw.rect(screen,self.top_color, self.top_rect,border_radius = self.radius//2)
        screen.blit(self.text_surf, self.text_rect)


    def handle_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            if pygame.mouse.get_pressed()[0]:
                self.dynamic_elevation = 0
                self.pressed = True
            else:
                self.dynamic_elevation = self.elevation
                if self.pressed == True:
                    self.pressed = False
                    self.strength = (self.strength + 1) % self.max_strength
        else:
            self.dynamic_elevation = self.elevation
        self.top_color = self.strength_to_color[self.strength]
        self.text_surf = self.font.render(str(self.strength),True,'#FFFFFF')
        self.text_rect = self.text_surf.get_rect(center = self.top_rect.center)


    def reset_strength(self):
        self.strength = 0

