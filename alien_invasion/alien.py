import pygame
from  pygame.sprite import Sprite

class Alien(Sprite):
    """alien class"""

    def __init__(self, ai_game):
        """Initialize the alien starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        # load alien's image
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # load the alien's starting position
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # store the alien's exact position
        self.x = float(self.rect.x)

    def update(self):
        """Move the alien to the right"""
        self.x += self.settings.alien_speed * self.settings.fleet_direction
        self.rect.x = self.x

    def check_edges(self):
        """aliens at the edges of screen, return true"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True