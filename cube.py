import pygame

class Cube:
    def __init__(self, x, y, width, height) -> None:
        self.rect = pygame.rect.Rect(x, y, width, height)
        self.rect.center = (self.rect.width/2, self.rect.height/2)
        
        self.angle = 0
        
        self.color = (60, 0, 0)
        self.orgimg = pygame.surface.Surface((self.rect.x, self.rect.y))
        self.orgimg.fill(self.color)
        self.img = pygame.transform.rotate(self.orgimg, self.angle)
        self.rect = self.img.get_rect()

    def draw(self, screen):
        screen.blit(self.img, (self.rect.x, self.rect.y))