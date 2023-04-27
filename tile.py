import pygame
from settings import *

class Mur(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/png/obstacle/mur_stone.png').convert_alpha() # texture du rocher à changer
        self.rect = self.image.get_rect(topleft = pos)
        self.hitbox = self.rect.inflate(0,0)
        