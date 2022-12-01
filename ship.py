import pygame


class Ship:
    """A class to manage the ship.
    The Ship class controls all attributes of the ship
    """

    def __init__(self,ai_game):
        """Initialize the ship and set its starting position."""
        self.screen=ai_game.screen
        self.screen_rect=ai_game.screen.get_rect()

        self.ship_image=pygame.image.load('images/ship.bmp')
        self.ship_rect=self.ship_image.get_rect()
        self.ship_rect.midbottom=self.screen_rect.midbottom

        #Movement flag
        self.moving_right=False
        self.moving_left=False

    def update(self):
        if self.moving_right:
            self.ship_rect.x+=1
        if self.moving_left:
            self.ship_rect.x-=1


    def blitme(self):
        self.screen.blit(self.ship_image,self.ship_rect)
