import pygame
from pygame import *
from player import Player
from wall import *

class Game(object):
    def main(self, screen):
        clock = pygame.time.Clock()

        #background = pygame.image.load("background_image_file")
        self.sprites = pygame.sprite.Group()
        self.player = Player(self.sprites) 
        self.walls = pygame.sprite.Group()
        self.wall = Wall(self,self.sprites)
        Wall.draw_border(Wall,self)

        while 1:
            clock.tick(30)
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return


            self.sprites.update(dt/1000)
            screen.fill((200,200,200))
            #screen.blit((0,0),background)            
            self.sprites.draw(screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    running = True
    Game().main(screen)

