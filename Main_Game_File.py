### Main Game File

import pygame
import sys
import Tower_Selection_Window as selection
import Game_Window as window
import Mouse_pos as mouse


pygame.init()

pygame.display.set_caption("Tower Defence")

background_img = pygame.image.load("Sprites\\background.bmp")
background_img = pygame.transform.scale(background_img,(window.WINDOW_WIDTH,window.WINDOW_HEIGHT))

BLACK = (0,0,0)
WHITE = (255,255,255)

clock = pygame.time.Clock()



def main_game_loop():

    game_loop = True

    while game_loop:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                game_loop = False

        
        window.game_window.blit(background_img,[0,0])
        selection.Tower_Selection.Tower_Draw()
        print(mouse.mouse_pressed(selection.Tower_select_group))
        selection.Tower_select_group.draw(window.game_window)
        selection.Tower_select_group.update()
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
   
    

main_game_loop()




    
