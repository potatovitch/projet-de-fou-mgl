import pygame
from settings import *
from player import Player
from tile import Mur
from debug import debug

class Level:
    def __init__(self):
        
        # get the display surface
        self.display_surface = pygame.display.get_surface()
        
        # sprite group setup
        self.visible_sprites = YSortCameraGroup()
        self.obstacle_sprites = pygame.sprite.Group()
        
        # sprite setup
        self.create_map()
    
    def create_map(self):
        for indice_ligne,ligne in enumerate(WORLD_MAP):
            for indice_col, col in enumerate(ligne):
                x = indice_col * TILESIZE
                y = indice_ligne * TILESIZE
                
                if col == 'x' :
                    Mur((x,y),[self.visible_sprites, self.obstacle_sprites]) # place sol en stone
                    
                if col == 'p':
                    self.player = Player((x,y),[self.visible_sprites], self.obstacle_sprites) # place player
                
                
    def run(self):
        # update and draw the game
        self.visible_sprites.custom_draw(self.player)
        self.visible_sprites.update()
        debug(self.player.direction)
        
        
class YSortCameraGroup(pygame.sprite.Group):
    def __init__(self):
        
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2
        self.half_height = self.display_surface.get_size()[1] // 2
        self.offset = pygame.math.Vector2()
        
        
    def custom_draw(self, player):
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height
        
        for sprite in sorted(self.sprites(), key = lambda sprite: sprite.rect.centery):
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)