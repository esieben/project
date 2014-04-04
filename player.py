import pygame
from pygame import *

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player,self).__init__(*groups)
        self.image = pygame.image.load("player.png")
        self.rect = pygame.rect.Rect((320,240), self.image.get_size())

    def update(self,dt):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 200 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 200 * dt
        if key[pygame.K_UP]:
            self.rect.y -= 200 * dt
        if key[pygame.K_DOWN]:
            self.rect.y += 200 * dt
