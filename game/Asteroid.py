import pygame


class Asteroid(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([30,30])
        self.rect = self.image.get_rect()
        self.rect.x = 30
        self.rect.y = 0

    def fallDown(self, dy=10):
        self.rect.y += dy
        if self.rect.y >= 400 :
            self.rect.y = 0

    def setCoord_X(self, x):
        self.rect.x = x

    def setCoord_Y(self, y):
        self.rect.y = y

    def isBeyond(self):
        return self.rect.y >= 396
    def getRect(self):
        return self.rect