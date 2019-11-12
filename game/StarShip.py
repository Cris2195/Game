import pygame


class Starship(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([60,60])
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 250

    def moveToRight(self, dx=5):
        self.rect.x += dx

    def moveToLeft(self,dx):
        self.rect.x -= dx

    def getRect(self):
        return self.rect

