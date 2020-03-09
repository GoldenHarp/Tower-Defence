### Main Game File

import pygame
import sys

pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
game_window = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
pygame.display.set_caption("Tower Defence")

background_img = pygame.image.load("C:\\Users\\darem\\Documents\\GitHub\\Tower-Defence\\Sprites\\background.bmp")
bacground_img = pygame.transform.scale(background_img,(WINDOW_WIDTH,WINDOW_HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()





def main_game_loop():

    game_loop = True

    while game_loop:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                game_loop = False

        game_window.fill(BLACK)
        game_window.blit(background_img,[0,0])
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
   
    

main_game_loop()




    
