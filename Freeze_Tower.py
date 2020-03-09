### Tower #2 Class



class Freeze_Tower(pygame.sprite.Sprite):


    def __init__(self,rect_x,rect_y,rad,attack_spd):
        super().__init__()

        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.rad = rad
        self.attack_spd = attack_spd



    def update(self):

        
