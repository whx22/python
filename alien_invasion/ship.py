import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        super().__init__()
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load the ship image and get its rect.
        self.image = pygame.image.load("images/ship.png")
        self.rect = self.image.get_rect()

        # Put every new ship at the bottom center of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # rect.x(int) x(float)
        self.x = float(self.rect.x)
        # moving status attribute of ship
        self.moving_right = False
        self.moving_left = False

    def blitem(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Adjust the ship's position based on the user's key behavior"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        elif self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)