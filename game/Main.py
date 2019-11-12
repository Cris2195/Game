import pygame
import sys
from StarShip import Starship
from Asteroid import Asteroid
from Missile import Missile
import random


def createAsteroids():
  lista = []
  b1 = Asteroid()
  b2 = Asteroid()
  b3 = Asteroid()
  lista.append(b1)
  lista.append(b2)
  lista.append(b3)
  return lista


def randomCoordToAsteroids(asteroids):
    w , h  = pygame.display.get_surface().get_size()
    asteroids.setCoord_Y(random.randint(1,100) )
    asteroids.setCoord_X(random.randint(1, 400)% w)


# initialize pygame
pygame.init()
# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLU = (0, 0, 255)
GREEN = (0, 255, 0)
list_of_colors = [BLACK, WHITE, RED, BLU, GREEN]
# load background image
bk = pygame.image.load("sfondo.png")
shuttle = pygame.image.load("rocket.png")
asteroid = pygame.image.load("asteroid.png")
missileimg = pygame.image.load("missile.png")
destroyed_asteroids = pygame.image.load("destroyed-planet.png")

# initialize screen game
size_screen = (width, heigth) = 415, 415
screen = pygame.display.set_mode(size_screen)
screen.blit(bk, (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
inGame = True
fire  = False
sprite_list = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()
sp = Starship()
sprite_list.add(sp)
missile = None
# set asteroid EVENT
b1 = Asteroid()
b2 = Asteroid()
b3 = Asteroid()
asteroids_group.add(b1)
asteroids_group.add(b2)
asteroids_group.add(b3)
pygame.time.set_timer(pygame.USEREVENT , 100)
while inGame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                sp.moveToRight(10)
            if event.key == pygame.K_LEFT:
                sp.moveToLeft(10)
            if event.key == pygame.K_SPACE:
                missile = Missile(sp.rect.x - 5, sp.rect.y - 5)
                fire = True
        elif event.type == pygame.USEREVENT:
            for asteroids in asteroids_group:
                if asteroids.isBeyond():
                    randomCoordToAsteroids(asteroids)
                else:
                    asteroids.fallDown(6)
    sprite_list.update()
    asteroids_group.update()
    collision = pygame.sprite.spritecollide(sp,asteroids_group,False)
    for c in collision:
        inGame=False
    if missile is not None:
        collisionMissile = pygame.sprite.spritecollide(missile , asteroids_group ,False)
        for coll in collisionMissile:
            screen.blit(bk, (0, 0))
            screen.blit(destroyed_asteroids , coll.getRect())
            pygame.display.flip()
            pygame.time.delay(200)
            asteroids_group.remove(coll)

    screen.blit(bk, (0, 0))
    if fire:
            missile.move()
            screen.blit(missileimg,missile.getRect())
    screen.blit(shuttle , sp.getRect())
    for x in asteroids_group:
        screen.blit(asteroid , x.getRect())

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
