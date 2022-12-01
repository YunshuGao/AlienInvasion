import pygame
from settings import Settings


class Ship:
    """A class to manage the ship.
    The Ship class controls all attributes of the ship
    """

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen=ai_game.screen
        self.settings=ai_game.settings
        self.screen_rect=ai_game.screen.get_rect()

        self.ship_image=pygame.image.load('images/ship.bmp')
        self.ship_rect=self.ship_image.get_rect()
        self.ship_rect.midbottom=self.screen_rect.midbottom

        #Store a decimal value for the ship's horizontal position.
        self.x=float(self.ship_rect.x)

        #Movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_right:
            self.x+=self.settings.ship_speed
        if self.moving_left:
            self.x-=self.settings.ship_speed
        #update rect object from self.x
        self.ship_rect.x=self.x


    def blitme(self):
        self.screen.blit(self.ship_image,self.ship_rect)
