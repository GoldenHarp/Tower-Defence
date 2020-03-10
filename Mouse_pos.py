### Mouse_pos

import pygame
import Tower_Selection_Window as selection




mpress = pygame.mouse.get_pressed()




def mouse_position(select_group):
    mpos = pygame.mouse.get_pos()
    print(mpos)
    for i in selection.Tower_select_group:
        if mpos[0] > i.rect.x and mpos [0]<i.rect.x +20 and mpos[1]> i.rect.y+30 and mpos[1]< i.rect.y :
            print("true")
            return True
    return False
    
    
