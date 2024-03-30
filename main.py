import pygame, sys
from pygame.locals import *
import playerScript

def rectCollision(Ax, Ay, Awidth, Aheight, Bx, By, Bwidth, Bheight):
    return (Ax + Awidth > Bx) and (Ax < Bx + Bwidth) and (Ay + Aheight > By) and (Ay < By + Bheight)


class gameClass:
    def __init__(self) -> None:
        self.Clock = pygame.time.Clock()
        self.r = True
        self.size = [700, 700]
        self.screen = pygame.display.set_mode(self.size)
        self.player = playerScript.Player(400, 400, True)
        self.player2 = playerScript.Player(200, 200, False)
        self.deltaTime = 0
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
        for bullet in self.player.bullets:
            if True == rectCollision(bullet.pos[0], bullet.pos[1], bullet.size[0], bullet.size[1],
                            self.player2.pos[0], self.player2.pos[1], self.player2.size[0], self.player2.size[1]):
                self.player2 = playerScript.Player(200, 200, False)
        for bullet in self.player2.bullets:
            if True == rectCollision(bullet.pos[0], bullet.pos[1], bullet.size[0], bullet.size[1],
                            self.player.pos[0], self.player.pos[1], self.player.size[0], self.player.size[1]):
                self.player = playerScript.Player(400, 400, True)
        return 0 
    def render(self):
        self.screen.fill((255, 255, 255))
        self.player.update(self.deltaTime)
        self.player.draw(self.screen)
        self.player2.update(self.deltaTime)
        self.player2.draw(self.screen)
        
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