import pygame
from pygame import *
from player import Player
from wall import *
from pixelmap import *

class Game(object):
    def main(self, screen):
        self.screen = screen
        clock = pygame.time.Clock()
        self.p = Pixelmap("wall.png",32,32)
        self.p.load_from_file("index.png")
        
        #initialize variables to allow map scrolling
        #x increases from left right, y increases from top to bottom
        self.screen_position_x = 0
        self.screen_position_y = 0
        self.wall_positions = self.p.get_object_position(self, Wall)


        #background = pygame.image.load("background_image_file")
        self.sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        for x,y in self.wall_positions:
            self.walls.add(Wall(x,y,self.sprites))
        self.player = Player(self.sprites) 
            
        while 1:
            clock.tick(30)
            dt = clock.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return


            self.wall_positions = self.p.get_object_position(self, Wall)
            self.sprites.update(dt/1000, self)
            self.screen.fill((200,200,200))
            #screen.blit((0,0),background)            
            self.sprites.draw(self.screen)
            pygame.display.flip()

if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((640,640))
    running = True
    Game().main(screen)

