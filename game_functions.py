import sys          # to exit the game when player quits the game, use sys package
import pygame       # for functionality needed to build the game

def events_check(spaceShip):

    # respond to keyboard and mouse events. to access events detected by Pygame use pygame.event.get()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()  # Quit the game.

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Move the ship to the right
                spaceShip.moving_right = True
            elif event.key == pygame.K_LEFT:
                #Move the ship to the left
                spaceShip.moving_left = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                spaceShip.moving_right = False
            if event.key == pygame.K_LEFT:
                spaceShip.moving_left = False


def screen_update(screen, gameSettings, spaceShip):
    screen.fill(gameSettings.background_color)
    spaceShip.draw()

    pygame.display.flip()       # tell Pygame to make the most recently drawn screen visible