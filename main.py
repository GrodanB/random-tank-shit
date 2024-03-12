import pygame, sys
from pygame.locals import *
import cube

class gameClass:
    def __init__(self) -> None:
        self.r = True
        self.size = [700, 700]
        self.screen = pygame.display.set_mode(self.size)
        self.cubes = [cube.Cube(200, 200, 50, 50)]
    def handleEvent(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.r = False
    def update(self):
        return 0 
    def render(self):
        for cube in self.cubes:
            cube.draw(self.screen)
        pygame.time.Clock().tick(60)
        pygame.display.update()

def main():
    game = gameClass()
    while game.r == True:
        game.handleEvent()
        game.update()
        game.render()
    pygame.exit()
    return 0 
sys.exit(main())