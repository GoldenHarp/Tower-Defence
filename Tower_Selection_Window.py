### Tower_Selection_Window



Tower_Selection = pygame.image.load("C:\\Users\\darem\\Documents\\GitHub\\Tower-Defence\\Sprites\\Tower_Selection_img.bmp")
Tower_Selection = pygame.transform.scale(Tower_Selection,(100,300))


def Tower_selection():
    game_window.blit(Tower_Selection,[100,100])
