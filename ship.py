import pygame
from settings import Settings


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        """Initialize the ship and set its starting position."""
        self.settings = Settings()

        # Movement flag
        self.moving_right = False
        self.moving_left = False

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.settings = ai_game.settings



        # Load the ship image and get its rect.
        self.image = pygame.image.load('images/space-ship-small.jpg')
        # self.image = pygame.transform.scale(image,
        #                                     (self.settings.screen_width / self.settings.ship_scale,
        #                                      self.settings.screen_height / self.settings.ship_scale))

        self.rect = self.image.get_rect()

        # Store a decimal value for the ship's horizontal position.
        self.x = float(self.rect.x)

        # Start each new ship at the bottom center of the screen.

        self.rect.midbottom = self.screen_rect.midbottom

    def update(self):
        """Update the ship's position based on the movement flag."""
        if self.moving_right:
            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
