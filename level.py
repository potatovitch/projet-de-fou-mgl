import pygame
from settings import *
from tile import Rocher, Eau
from sol import Sable, Grass

class Level:
    def __init__(self):
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacles_sprites = pygame.sprite.Group()
        
        # sprite setup
        self.create_map()
    
    def create_map(self):
        for indice_ligne,ligne in enumerate(WORLD_MAP):
            for indice_col, col in enumerate(ligne):
                x = indice_col * TILESIZE
                y = indice_ligne * TILESIZE
                if col == 'x' :
                    Rocher((x,y),[self.visible_sprites])   # place caillou
                if col == 's':
                    Sable((x,y),[self.visible_sprites]) # place sable
                if col == 'g':
                    Grass((x,y),[self.visible_sprites]) # place grass
                if col == 'e':
                    Eau((x,y),[self.visible_sprites]) # place eau
                
    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)