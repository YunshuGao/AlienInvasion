import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    """A class to manage bullets fried from the ship"""

    def __init__(self,ai_game):
        """Creating a bullet object at the ship's current position."""
        super().__init__()
        self.bullet_screen=ai_game.screen
        self.settings=ai_game.settings
        self.bullet_color=self.settings.bullet_color

        # Create a bullet rect at(0,0) and then set correct position.
        self.bullet_rect=pygame.Rect(0,0,self.settings.bullet_width,self.settings.bullet_height)
        self.bullet_rect.midtop=ai_game.ship.ship_rect.midtop

        #Store the bullet's postion as a decimal value
        self.y=float(self.bullet_rect.y)

    def update(self):
        """Move the bullet up the screen"""
        # Update the decimal position of the bullet
        self.y-=self.settings.bullet_speed
        #Update the rect position
        self.bullet_rect.y=self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.bullet_screen,self.bullet_color,self.bullet_rect)



