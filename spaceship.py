import pygame

class Spaceship:

    def __init__(self, screen):         # screen on which we draw the ship

        self.screen = screen

        # to load image use pygame.image.load(), it returns a surface representing the ship
        self.image = pygame.image.load("spaceship.png")
        # additional step to resize the image
        self.image = pygame.transform.scale(self.image, (300, 180))

        # get_rect() --> allows to access the suface's rect attribute
        """
        Pygame lets user treat game elements as rectangles, even if they are not 
        shaped as a rectangle.
        """
        self.ship_rect = self.image.get_rect()

        # screen's rect attributes
        self.screen_rect = self.screen.get_rect()

        # placing the ship at the bottom center of the screen
        self.ship_rect.centerx = self.screen_rect.centerx
        self.ship_rect.bottom = self.screen_rect.bottom

        # Movement Flags
        self.moving_right = False
        self.moving_left = False


    def update(self):

        if self.moving_right:
            self.ship_rect.centerx += 1

        if self.moving_left:
            self.ship_rect.centerx -= 1

    def draw(self):

        #draw the spaceship at the position specified by ship_rect
        self.screen.blit(self.image, self.ship_rect)