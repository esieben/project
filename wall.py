import pygame
from pygame import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, game,*groups):
        super(Wall,self).__init__(*groups)
        self.image = pygame.image.load("wall.png")
    
    def draw_border(self,game):                
        for x in range(0,640,32):
            for y in range(0,480,32):
                if x in (0,640-32) or y in (0,480-32):                     
                    wall = pygame.sprite.Sprite()
                    self.image = pygame.image.load("wall.png")
                    game.walls.add(wall)   
                    self.rect = pygame.rect.Rect((x,y),self.image.get_size())
            game.sprites.add(game.walls)
