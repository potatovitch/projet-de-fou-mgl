import pygame
from settings import *

class Rocher(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/png/grocaillou.png').convert_alpha() # texture du rocher à changer
        self.rect = self.image.get_rect(topleft = pos)
        
class Eau(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/test/eau.png').convert_alpha() # texture de l'eau à changer
        self.rect = self.image.get_rect(topleft = pos)


