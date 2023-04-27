import pygame
from settings import *
from player import Player
from tile import Mur, Eau
from sol import Sable, Grass, Stone, Planche
from debug import debug

class Level:
    def __init__(self):
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = pygame.sprite.Group()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # sprite setup
        self.create_map()
    
    def create_map(self):
        for indice_ligne,ligne in enumerate(WORLD_MAP):
            for indice_col, col in enumerate(ligne):
                x = indice_col * TILESIZE
                y = indice_ligne * TILESIZE
                if col == 'x' :
                    Stone((x,y),[self.visible_sprites]) # place sol en stone
                if col == 's':
                    Sable((x,y),[self.visible_sprites]) # place sable
                if col == 'g':
                    Grass((x,y),[self.visible_sprites]) # place grass
                if col == 'e':
                    Eau((x,y),[self.visible_sprites, self.obstacle_sprites]) # place eau
                if col == 'm':
                    Mur((x,y),[self.visible_sprites, self.obstacle_sprites]) # place mur
                if col == 'y':
                    Planche((x,y),[self.visible_sprites]) # place planche
                    
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites) # place player
                
                
    def run(self):
        # update and draw the game
        self.visible_sprites.draw(self.display_surface)
        self.visible_sprites.update()
        debug(self.player.direction)