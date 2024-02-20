import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """Manage all of bullets"""

    def __init__(self, ai_game):
        """Creating a bullets at the position of current ship"""
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = ai_game.settings.bullet_color

        # Creating a bullet and setting its position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # y position of the current bullet
        self.y = float(self.rect.y)

    def update(self):
        """bullet y position moving"""
        self.y -= self.settings.bullet_speed
        # update bullet position on screen
        self.rect.y = self.y

    def draw_bullet(self):
        """draw bullet on screen"""
        pygame.draw.rect(self.screen, self.settings.bullet_color, self.rect)