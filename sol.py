import pygame
from settings import *

class Grass(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/png/sol/light_grass.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
class Sable(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/png/sol/sable_chelou.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
class Stone(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/png/sol/stone1.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)
        
class Planche(pygame.sprite.Sprite):
    def __init__(self,pos,groups):
        super().__init__(groups)
        self.image = pygame.image.load('../graphics/png/sol/planche.png').convert_alpha()
        self.rect = self.image.get_rect(topleft = pos)