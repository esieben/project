import pygame
from pygame import *
from pixelmap import *
from wall import *

class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player,self).__init__(*groups)
        self.image = pygame.image.load("player.png")
        self.rect = pygame.rect.Rect((320,240), self.image.get_size())

    def update(self,dt,game):
        print (game.screen_position_y)
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 200 * dt
            if self.rect.x < 40:
                game.screen_position_x -= 1
                self.rect.x += 600
        if key[pygame.K_RIGHT]:
            self.rect.x += 200 * dt
            if self.rect.x > 600:
                game.screen_position_x += 1
                self.rect.x -=600
        if key[pygame.K_UP]:
            self.rect.y -= 200 * dt
            if self.rect.y < 40:
                game.screen_position_y -= 1
                self.rect.y += 600
        if key[pygame.K_DOWN]:
            self.rect.y += 200 * dt
            if self.rect.y > 600:
                game.screen_position_y += 1
                self.rect.y -= 600

        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last
