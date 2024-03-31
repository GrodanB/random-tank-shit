import pygame, sys
from pygame.locals import *
import playerScript
import setup
def rectCollision(Ax, Ay, Awidth, Aheight, Bx, By, Bwidth, Bheight):
    return (Ax + Awidth > Bx) and (Ax < Bx + Bwidth) and (Ay + Aheight > By) and (Ay < By + Bheight)


class gameClass:
    def __init__(self) -> None:
        self.Clock = pygame.time.Clock()
        self.r = True
        self.screenSize = [640, 640]
        self.screen = pygame.display.set_mode(self.screenSize)
        self.player = playerScript.Player(400, 400, 1, True)
        self.player2 = playerScript.Player(200, 200, 1, False)
        self.deltaTime = 0
        self.MapObj = setup.Map(1)
        self.MapObj.loadMap()
    def handleEvent(self):
        if pygame.event.get(QUIT):
            self.r = False
        for event in pygame.event.get(KEYDOWN):
            #player1
            if event.key == K_w:
                self.player.updateVal(speed=.25)
            if event.key == K_s:
                self.player.updateVal(speed=-.25)
            if event.key == K_a:
                self.player.updateVal(angle=.125)
            if event.key == K_d:
                self.player.updateVal(angle=-.125)
            if event.key == K_SPACE:
                self.player.shoot()

            #player2
            if event.key == K_UP:
                self.player2.updateVal(speed=.25)
            if event.key == K_DOWN:
                self.player2.updateVal(speed=-.25)
            if event.key == K_LEFT:
                self.player2.updateVal(angle=.125)
            if event.key == K_RIGHT:
                self.player2.updateVal(angle=-.125)
            if event.key == K_RSHIFT:
                self.player2.shoot()
        for event in pygame.event.get(KEYUP):
            if event.key == K_w:
                self.player.updateVal(speed=-.25)
            if event.key == K_s:
                self.player.updateVal(speed=.25)
            if event.key == K_a:
                self.player.updateVal(angle=-.125)
            if event.key == K_d:
                self.player.updateVal(angle=.125)
            if event.key == K_UP:
                self.player2.updateVal(speed=-.25)
            if event.key == K_DOWN:
                self.player2.updateVal(speed=.25)
            if event.key == K_LEFT:
                self.player2.updateVal(angle=-.125)
            if event.key == K_RIGHT:
                self.player2.updateVal(angle=.125)
    def update(self):
        self.player.update(self.deltaTime)
        if self.player.getVal(pos=1)[0] < 0:
            self.player.updateVal(x=0)
        if self.player.getVal(pos=1)[1] < 0:
            self.player.updateVal(y=0)
        
        if self.player.getVal(pos=1)[0] + self.player.getVal(size=1)[0] > self.screenSize[0]:
            self.player.updateVal(x=self.screenSize[0]-self.player.getVal(size=1)[0])
        if self.player.getVal(pos=1)[1] + self.player.getVal(size=1)[1] > self.screenSize[1]:
            self.player.updateVal(y=self.screenSize[1]-self.player.getVal(size=1)[1])
        
        self.player2.update(self.deltaTime)
        if self.player2.getVal(pos=1)[0] < 0:
            self.player2.updateVal(x=0)
        if self.player2.getVal(pos=1)[1] < 0:
            self.player2.updateVal(y=0)
        
        if self.player2.getVal(pos=1)[0] + self.player2.getVal(size=1)[0] > self.screenSize[0]:
            self.player2.updateVal(x=self.screenSize[0]-self.player2.getVal(size=1)[0])
        if self.player2.getVal(pos=1)[1] + self.player2.getVal(size=1)[1] > self.screenSize[1]:
            self.player2.updateVal(y=self.screenSize[1]-self.player2.getVal(size=1)[1])


        for bullet in self.player.bullets:
            if True == rectCollision(bullet.pos[0], bullet.pos[1], bullet.size[0], bullet.size[1],
                            self.player2.pos[0], self.player2.pos[1], self.player2.size[0], self.player2.size[1]):
                self.player2 = playerScript.Player(200, 200, self.player2.scale, False)
        for bullet in self.player2.bullets:
            if True == rectCollision(bullet.pos[0], bullet.pos[1], bullet.size[0], bullet.size[1],
                            self.player.pos[0], self.player.pos[1], self.player.size[0], self.player.size[1]):
                self.player = playerScript.Player(400, 400, self.player.scale,  True)
        return 0 
    def render(self):
        self.screen.fill((255, 255, 255))
        
        self.player.draw(self.screen)

        self.player2.draw(self.screen)
        
        self.MapObj.draw(self.screen)

        self.deltaTime = self.Clock.get_time()
        self.Clock.tick(60)
        
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