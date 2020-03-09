### Tower_Selection_Window

import pygame
import Game_Window as window

pygame.init()



Tower_Selection_img = pygame.image.load("C:\\Users\\darem\\Documents\\GitHub\\Tower-Defence\\Sprites\\Tower_Selection_img.bmp")
Tower_Selection_img = pygame.transform.scale(Tower_Selection_img,(200,300))
Freeze_Tower_img = pygame.image.load("C:\\Users\\darem\\Documents\\GitHub\\Tower-Defence\\Sprites\\Freeze_Tower.bmp")
Freeze_Tower_img = pygame.transform.scale(Freeze_Tower_img,(30,30))


def Tower_Selection():
    window.game_window.blit(Tower_Selection_img,[10,10])
    window.game_window.blit(Freeze_Tower_img,[30,20])
