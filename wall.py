import pygame
from pygame import *
from pixelmap import *

class Wall(pygame.sprite.Sprite):
    def __init__(self,x,y,*groups):
        super(Wall,self).__init__(*groups)
        self.image = pygame.image.load("wall.png")
        self.rect = pygame.rect.Rect((x,y), self.image.get_size())
    