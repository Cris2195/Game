import pygame


class Missile(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Missile, self).__init__()
        self.image = pygame.Surface([30, 30])
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def move(self):
        self.rect.y -= 5

    def getRect(self):
        return self.rect
