import pygame, math

class Player:
    def __init__(self, x, y, one) -> None:
        self.size = [65, 50]
        self.rect = pygame.rect.Rect(x, y, 65, 50)
        #needed because of shity rounding from rect.x being an int
        self.pos: float = [x, y]
        self.rect.center = (self.rect.width/2, self.rect.height/2)
        self.angle = 0
        self.oldAngle = self.angle
        self.changeangle = 0
        self.speed = 0
        self.bullets = []
        #Making tank
        #main Surf
        orgimg = pygame.image.load("data/img/tank.png")
        if one == True:
            self.orgimg = orgimg.subsurface((0, 0), (65, 50))
        else:
            self.orgimg = orgimg.subsurface((65, 0), (65, 50))
        #self.orgimg = pygame.surface.Surface((self.rect.width, self.rect.height)).convert_alpha()
        ##Barrel surf
        #self.barrel = pygame.surface.Surface((50, 10))
        #self.barrel.fill((self.color[0]*.75, self.color[1]*.75, self.color[2]*.75))
        ##Body Surf
        #self.body = pygame.surface.Surface((50, 50))
        #self.body.fill(self.color)
        #
        ##filling surf
        #self.orgimg.blit(self.body, (0, 0))
        #self.orgimg.blit(self.barrel, (15, 20))

        self.img = pygame.transform.rotate(self.orgimg, self.angle)
        self.rect = self.img.get_rect()

    def updateVal(self, speed=None, x=None, y=None, angle=None):

        if angle != None:
            self.changeangle += angle
        if speed != None:
            self.speed += speed
        if x != None:
            self.rect.x = x
        if y != None:
            self.rect.y = y

    def update(self, deltaTime):
        
        self.angle += round(self.changeangle * deltaTime)
        if self.angle != self.oldAngle:
            size = self.rect.size
            self.img = pygame.transform.rotate(self.orgimg, self.angle)
            Topleft = [size[0]/2 + self.pos[0] - self.img.get_width()/2,  #X
                       size[1]/2 + self.pos[1] - self.img.get_height()/2] #Y
            self.pos = Topleft
            self.rect = self.img.get_rect(topleft = Topleft)
            self.oldAngle = self.angle
        self.pos[0] += math.cos(math.radians(self.angle)) * self.speed*deltaTime
        self.pos[1] -= math.sin(math.radians(self.angle)) * self.speed*deltaTime

        self.rect.x = self.pos[0]
        self.rect.y = self.pos[1]
        for Bullet in self.bullets:
            Bullet.update(deltaTime)
    def draw(self, screen): 
        screen.blit(self.img.convert_alpha(), self.rect)
        for Bullet in self.bullets:
            Bullet.draw(screen)
    def shoot(self):
        pos = [0, 0]
        pos[0] = self.rect.centerx + math.cos(math.radians(self.angle)) * (60/2)
        pos[1] = self.rect.centery - math.sin(math.radians(self.angle)) * (60/2)
        self.bullets.append(bullet(pos, self.angle, .5, self))
        
class bullet:
    def __init__(self, pos, angle, speed, owner) -> None:
        self.pos = pos
        self.angle = angle
        self.speed = speed
        self.size = [3, 3]
        self.orgimg = pygame.surface.Surface(self.size)
        self.orgimg.fill((0, 0, 0))
        self.img = pygame.transform.rotate(self.orgimg, self.angle).convert_alpha()
        self.owner = owner
    def draw(self, screen):
        screen.blit(self.img, self.pos)
    def update(self, deltaTime):
        self.pos[0] += math.cos(math.radians(self.angle)) * self.speed*deltaTime
        self.pos[1] -= math.sin(math.radians(self.angle)) * self.speed*deltaTime