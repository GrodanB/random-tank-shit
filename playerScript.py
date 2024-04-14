import pygame, math

class Rectangle:
    def __init__(self, img: pygame.Surface, scale, angle, offsetDistance, staticOffset=[0, 0]):
        self.orgimg: pygame.Surface = img.convert_alpha()
        self.rect: pygame.Rect = img.get_rect()
        self.scale = scale
        self.angle = angle
        self.offsetDistance = offsetDistance
        self.staticOffset = staticOffset
        self.offset = [0, 0]


        self.orgimg = pygame.transform.scale(self.orgimg, (self.rect.width*self.scale, self.rect.height*self.scale))
        self.img = pygame.transform.rotate(self.orgimg, self.angle)
        self.rotCenter()
        self.getOffset()
    def rotCenter(self):
        self.img = pygame.transform.rotate(self.orgimg, self.angle).convert_alpha()
        return self.img
    def getOffset(self):
        self.offset = [(math.cos(math.radians(self.angle))*self.offsetDistance), -(math.sin(math.radians(self.angle))*self.offsetDistance)]
        return self.offset
    def update(self, angle):
        if self.angle != angle:
            self.rotCenter()
            self.getOffset()
            self.angle = angle
    def draw(self, screen: pygame.surface, pos: list):
        screen.blit(self.img, (pos[0] + self.offset[0] - self.img.get_width()/2, pos[1] + self.offset[1] - self.img.get_height()/2))

class Player:
    def __init__(self, x, y, scale, one, bullets) -> None:
        self.scale = scale
        self.size = [65*self.scale, 50*self.scale]
        self.tanksize = [50*self.scale, 50*self.scale]
        self.one = one
        self.pos = [x, y]
        self.angle = 0
        self.oldAngle = self.angle
        self.changeangle = 0
        self.speed = 0
        self.bullets = bullets
        #Making tank
        self.TurretOffset = [0, 0]
        self.CanonOffset = [0, 0]
        #main Surf
        Baseorgimg = pygame.image.load("data/img/Tanks.png")
        Turretorgimg = pygame.image.load("data/img/turrets.png")
        Canonorgimg = pygame.image.load("data/img/canons.png")
        
        if one == True:
            Baseorgimg = Baseorgimg.subsurface((0, 0), (50, 50))
            Turretorgimg = Turretorgimg.subsurface((0, 0), (31, 24))
            Canonorgimg = Canonorgimg.subsurface((0, 0), (27, 10))
        
        else:
            Baseorgimg = Baseorgimg.subsurface((0, 50), (50, 50))
            Turretorgimg = Turretorgimg.subsurface((0, 24), (31, 24))
            Canonorgimg = Canonorgimg.subsurface((0, 10), (27, 10))
        
        self.Base = Rectangle(Baseorgimg, self.scale, 0, 0)
        self.Turret = Rectangle(Turretorgimg, self.scale, 0, .5)
        self.Canon = Rectangle(Canonorgimg, self.scale, 0, 26)

    def updateVal(self, speed=None, x=None, y=None, angle=None, pos=None):

        if angle != None:
            self.changeangle = angle
        if speed != None:
            self.speed = speed
        if x != None:
            self.pos[0] = x
        if y != None:
            self.pos[1] = y
        if pos != None:
            self.pos = pos
    
    def getVal(self, speed=None, x=None, y=None, angle=None, pos=None, size=None):
        #Can only give ONE variable
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
            return [self.Base.img.get_width(), self.Base.img.get_height()]
    
    
    def update(self, deltaTime):
        
        self.angle += round(self.changeangle * deltaTime)
        
        self.Base.update(self.angle)
        self.Turret.update(self.angle)
        self.Canon.update(self.angle)
        
        self.pos[0] += math.cos(math.radians(self.angle)) * self.speed*self.scale*deltaTime
        self.pos[1] -= math.sin(math.radians(self.angle)) * self.speed*self.scale*deltaTime

        for Bullet in self.bullets:
            Bullet.update(deltaTime)

    def draw(self, screen): 

        pos = [self.pos[0] + self.tanksize[0]/2, self.pos[1] + self.tanksize[1]/2]
        self.Base.draw(screen, pos)

        self.Turret.draw(screen, pos)
        self.Canon.draw(screen, pos)
        for Bullet in self.bullets:
            Bullet.draw(screen)

    def shoot(self):
        
        pos = [0, 0]
        pos[0] = self.pos[0] + self.Canon.offset[0] + self.tanksize[0]/2 + math.cos(math.radians(self.angle)) * (self.Canon.orgimg.get_width()/2)
        pos[1] = self.pos[1] + self.Canon.offset[1] + self.tanksize[1]/2 - math.sin(math.radians(self.angle)) * (self.Canon.orgimg.get_width()/2)
        self.bullets.append(bullet(pos, self.angle, .13, self, self.scale))
        



class bullet:
    def __init__(self, pos, angle, speed, owner, scale) -> None:
        self.pos = pos
        self.age = 0
        self.flipped = [False, False]
        self.flippedTime = [0, 0]
        self.scale = scale
        self.angle = angle
        self.speed = speed
        self.size = [5*self.scale, 5*self.scale]
        self.orgimg = pygame.surface.Surface(self.size).convert_alpha()
        self.orgimg.fill((0, 0, 0, 255))
        
        self.img = pygame.transform.rotate(self.orgimg, self.angle).convert_alpha()
        self.owner = owner
    def draw(self, screen):
        screen.blit(self.img, self.pos)
    def update(self, deltaTime):
        self.flippedTime[0] -= 1
        self.flippedTime[1] -= 1
        self.age += 1
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