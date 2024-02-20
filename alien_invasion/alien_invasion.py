"""
sys is a module
that provides access to some variables used or maintained
by the interpreter and to functions that interact strongly with the interpreter.
"""
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.settings = Settings()
        # fullscreen setting: add pygame.FULLSCREEN attribute
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        # ship object
        self.ship = Ship(self)
        # bullet object
        self.bullets = pygame.sprite.Group()

    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_screen()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)

    def _check_keydown_events(self, event):
        """key down respond"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_event(self, event):
        """key up respond"""
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        # Redraw the screen
        self.screen.fill(self.settings.bg_color)
        self.ship.blitem()
        # update every bullet
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Make the most recently drawn screen visible.
        pygame.display.flip()

    def _update_bullets(self):
        """
        delete over margin bullets
        for loop must traverse over a fixed length list
        """
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

    def _fire_bullet(self):
        """Creating a new bullet"""
        if len(self.bullets) <= self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)



if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()