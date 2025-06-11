# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init() # initialize pygame
    pygame.time.Clock() # create a clock object to control the frame rate
    dt = 0 # delta time 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    player = Player(x = SCREEN_WIDTH / 2, y = SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill((0, 0, 0)) # fill with black
        player.update(dt)
        player.draw(screen) # draw the player on the screen
        pygame.display.flip() # call this last !
        
        dt = pygame.time.Clock().tick(60)/1000 # limit to 60 FPS
        
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

if __name__ == "__main__":
    main()