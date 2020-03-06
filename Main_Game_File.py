### Main Game File

import pygame
import sys

pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defence")

BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()





def main_game_loop():

    game_loop = True

    while game_loop:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                game_loop = False

        pygame.display.update()
        clock.tick(60)
    pygame.quit()
   
    



main_game_loop()




    
