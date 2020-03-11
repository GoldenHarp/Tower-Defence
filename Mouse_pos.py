### Mouse_pos

import pygame
import Tower_Selection_Window as selection

WHITE = (255,255,255)



def mouse_pressed(select_group):
    mpress = pygame.mouse.get_pressed()
    print(mpress)
    mpos = pygame.mouse.get_pos()
    for i in selection.Tower_select_group:
        if mpos[0] > i.rect.x and mpos [0]<i.rect.x +20 and mpos[1]< i.rect.y+30 and mpos[1]> i.rect.y and mpress == (1,0,0):
            i.rect.x = mpos[0]-15
            i.rect.y = mpos[1]-15
            return True
        
            
    return False
    
    
