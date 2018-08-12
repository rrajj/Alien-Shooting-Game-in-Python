import pygame                               # for functionality needed to build the game
from game_settings import GameSettings      # for game settings
from spaceship import Spaceship             # for the SpaceShip
import game_functions as gf                 # for the game functions/events
def run_game():
    # Initialize game and create a screen object
    pygame.init()
    # create a GameSettings object to make screen
    gameSettings = GameSettings()
    # make a screen with provided dimensions
    screen = pygame.display.set_mode((gameSettings.screen_width, gameSettings.screen_height))
    pygame.display.set_caption("Alien Shooting Game")

    # Draw the SpaceShip
    spaceShip = Spaceship(screen)


    # main loop to control the game
    while True:
        # use screen.fill to fill in the background color
        screen.fill(gameSettings.background_color)
        spaceShip.draw()
        gf.events_check(spaceShip)
        spaceShip.update()
        gf.screen_update(screen = screen, gameSettings = gameSettings, spaceShip = spaceShip)


run_game()          # initialize the game