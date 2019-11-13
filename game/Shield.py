import pygame


class Shield(pygame.sprite.Sprite):

    def __init__(self):
        super(Shield, self).__init__()
        self.image = pygame.Surface([30, 30])
        self.rect = self.image.get_rect()
        self.durata = 5000
        self.rect.x = 170
        self.rect.y = -60

    def getDurata(self):
        return self.durata

    def getRect(self):
        return self.rect
