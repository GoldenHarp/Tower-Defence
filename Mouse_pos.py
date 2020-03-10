### Mouse_pos

import pygame
import Tower_Selection_Window as selection



mpos = pygame.mouse.get_pos()
mpress = pygame.mouse.get_pressed()




def mouse_position():
    print(mpos)
    for i in selection.Tower_select_group:
        if mpos[0] > i.rect.x and mpos [1]<i.rect.x +20:
            print("true")
    
    
