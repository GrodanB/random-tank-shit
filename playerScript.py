import pygame, math

class Player:
    def __init__(self, x, y, scale, one, bullets) -> None:
        self.scale = scale
        self.size = [65*self.scale, 50*self.scale]
        self.tanksize = [50*self.scale, 50*self.scale]
        self.rect = pygame.rect.Rect(x, y, 65*self.scale, 50*self.scale)
        self.one = one
        #needed because of shity rounding from rect.x being an int
        self.pos: float = [x, y]
        self.rect.center = (self.rect.width/2, self.rect.height/2)
        self.angle = 0
        self.oldAngle = self.angle
        self.changeangle = 0
        self.speed = 0
        self.bullets = bullets
        #Making tank
        #main Surf
        orgimg = pygame.image.load("data/img/tank.png")
        if one == True:
            self.orgimg = orgimg.subsurface((0, 0), (65, 50))
        else:
            self.orgimg = orgimg.subsurface((65, 0), (65, 50))
        self.orgimg = pygame.transform.scale(self.orgimg, self.size)

        self.img = pygame.transform.rotate(self.orgimg, self.angle)
        self.rect = self.img.get_rect()
        self.rect.topleft = self.pos
    def updateVal(self, speed=None, x=None, y=None, angle=None, pos=None):

        if angle != None:
            self.changeangle = angle
        if speed != None:
            self.speed = speed
        if x != None:
            self.rect.x = x
            self.pos[0] = x
        if y != None:
            self.rect.y = y
            self.pos[1] = y
        if pos != None:
            self.pos = pos
    def getVal(self, speed=None, x=None, y=None, angle=None, pos=None, size=None):
        #Can only give ONE value/variable
        if angle != None:
            return self.angle
        if speed != None:
            return self.speed
        if x != None:
            return self.rect.x
        if y != None:
            return self.rect.y
        if pos != None:
            return self.pos
        if size != None:
            return [self.img.get_width(), self.img.get_height()]
    
    def update(self, deltaTime):
        
        self.angle += round(self.changeangle * deltaTime)
        
        if self.angle != self.oldAngle:
            size = self.rect.size
            self.img = pygame.transform.rotate(self.orgimg, self.angle)
            Topleft = [size[0]/2 + self.pos[0] - (self.img.get_width()/2),  #X
                       size[1]/2 + self.pos[1] - (self.img.get_height()/2)] #Y
            self.pos = Topleft
            self.rect = self.img.get_rect(topleft = Topleft)
            self.oldAngle = self.angle
        
        self.pos[0] += math.cos(math.radians(self.angle)) * self.speed*self.scale*deltaTime
        self.pos[1] -= math.sin(math.radians(self.angle)) * self.speed*self.scale*deltaTime

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
        pos[0] = self.rect.centerx + math.cos(math.radians(self.angle)) * (60*self.scale/2)
        pos[1] = self.rect.centery - math.sin(math.radians(self.angle)) * (60*self.scale/2)
        self.bullets.append(bullet(pos, self.angle, .13, self, self.scale))
        
class bullet:
    def __init__(self, pos, angle, speed, owner, scale) -> None:
        self.pos = pos
        self.flipped = [False, False]
        self.scale = scale
        self.angle = angle
        self.speed = speed
        self.size = [3*self.scale, 3*self.scale]
        self.orgimg = pygame.surface.Surface(self.size)
        self.orgimg.fill((0, 0, 0))
        self.img = pygame.transform.rotate(self.orgimg, self.angle).convert_alpha()
        self.owner = owner
    def draw(self, screen):
        screen.blit(self.img, self.pos)
    def update(self, deltaTime):
        
        if self.flipped[0] == False:
            self.pos[0] += math.cos(math.radians(self.angle)) * self.speed*self.scale*deltaTime
        else:
            self.pos[0] -= math.cos(math.radians(self.angle)) * self.speed*self.scale*deltaTime

        if self.flipped[1] == False:
            self.pos[1] -= math.sin(math.radians(self.angle)) * self.speed*self.scale*deltaTime
        else:
            self.pos[1] += math.sin(math.radians(self.angle)) * self.speed*self.scale*deltaTime
    
    def getVal(self, speed=None, x=None, y=None, angle=None, pos=None, size=None):
        #Can only give ONE value/variable
        if angle != None:
            return self.angle
        if speed != None:
            return self.speed
        if x != None:
            return self.pos[0]
        if y != None:
            return self.pos[1]
        if pos != None:
            return self.pos
        if size != None:
            return [self.img.get_width(), self.img.get_height()]