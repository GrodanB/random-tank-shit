import pygame, sys
from pygame.locals import *
import cube

class gameClass:
    def __init__(self) -> None:
        self.r = True
        self.size = [700, 700]
        self.screen = pygame.display.set_mode(self.size)
        self.player = cube.Player(400, 400, (200, 0, 0))
        self.player2 = cube.Player(200, 200, (0, 0, 200))
    def handleEvent(self):
        if pygame.event.get(QUIT):
            self.r = False
        for event in pygame.event.get(KEYDOWN):
            if event.key == K_w:
                self.player.updateVal(speed=4)
            if event.key == K_s:
                self.player.updateVal(speed=-4)
            if event.key == K_a:
                self.player.updateVal(angle=2)
            if event.key == K_d:
                self.player.updateVal(angle=-2)
            if event.key == K_UP:
                self.player2.updateVal(speed=4)
            if event.key == K_DOWN:
                self.player2.updateVal(speed=-4)
            if event.key == K_LEFT:
                self.player2.updateVal(angle=2)
            if event.key == K_RIGHT:
                self.player2.updateVal(angle=-2)
        for event in pygame.event.get(KEYUP):
            if event.key == K_w:
                self.player.updateVal(speed=-4)
            if event.key == K_s:
                self.player.updateVal(speed=4)
            if event.key == K_a:
                self.player.updateVal(angle=-2)
            if event.key == K_d:
                self.player.updateVal(angle=2)
            if event.key == K_UP:
                self.player2.updateVal(speed=-4)
            if event.key == K_DOWN:
                self.player2.updateVal(speed=4)
            if event.key == K_LEFT:
                self.player2.updateVal(angle=-2)
            if event.key == K_RIGHT:
                self.player2.updateVal(angle=2)
    def update(self):
        return 0 
    def render(self):
        self.screen.fill((255, 255, 255))
        #for cube in self.cubes:
        #    cube.draw(self.screen)
        #    cube.update()
        self.player.update()
        self.player.draw(self.screen)
        self.player2.update()
        self.player2.draw(self.screen)
        pygame.time.Clock().tick(60)
        pygame.display.update()

def main():
    game = gameClass()
    game.player.updateVal(x=400, y=400)
    while game.r == True:
        game.handleEvent()
        game.update()
        game.render()
    pygame.quit()
    return 0 
sys.exit(main())