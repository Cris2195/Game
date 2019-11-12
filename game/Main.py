import pygame
import sys
from StarShip import Starship
from Asteroid import Asteroid
from Missile import Missile
import random

# COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLU = (0, 0, 255)
GREEN = (0, 255, 0)
list_of_colors = [BLACK, WHITE, RED, BLU, GREEN]


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
    w, h = pygame.display.get_surface().get_size()
    asteroids.setCoord_Y(random.randint(1, 100))
    asteroids.setCoord_X(random.randint(1, 400) % w)


def getRandomCoord(*args):
    for elem in args:
        elem.setCoord_X(random.randint(1, 400))
        elem.setCoord_Y(random.randint(1, 100))


def menuFun(screen):
    font = pygame.font.SysFont("comicsansms", 40)
    text = font.render("Asteroid", True, random.choice(list_of_colors))
    screen.fill((255, 255, 255))
    screen.blit(text, (150, 150))
    pygame.display.flip()


def finishGame(risultato: str, screen):
    screen.fill(WHITE)
    if risultato == "YOU WON":
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("YOU WON ", True, random.choice(list_of_colors))
        screen.fill((255, 255, 255))
        screen.blit(text, (150, 150))
        pygame.display.flip()
        pygame.time.delay(1000)
    if risultato == "GAME OVER":
        font = pygame.font.SysFont("comicsansms", 40)
        text = font.render("GAME OVER", True, random.choice(list_of_colors))
        screen.fill((255, 255, 255))
        screen.blit(text, (150, 150))
        pygame.display.flip()
        pygame.time.delay(1000)


# initialize pygame
pygame.init()
# load background image
bk = pygame.image.load("sfondo.png")
shuttle = pygame.image.load("rocket.png")
asteroid = pygame.image.load("asteroid.png")
missileimg = pygame.image.load("missile.png")
destroyed_asteroids = pygame.image.load("destroyed-planet.png")

# initialize screen game
size_screen = (width, heigth) = 415, 415
screen = pygame.display.set_mode(size_screen)
menu = True;
while menu:
    menuFun(screen)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            inGame = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                menu = False

screen.blit(bk, (0, 0))
pygame.display.flip()
clock = pygame.time.Clock()
inGame = True
fire = False
sprite_list = pygame.sprite.Group()
asteroids_group = pygame.sprite.Group()
sp = Starship()
sprite_list.add(sp)
missile = None
# set asteroid EVENT
b1 = Asteroid()
b2 = Asteroid()
b3 = Asteroid()
b4 = Asteroid()
b5 = Asteroid()
getRandomCoord(b1,b2,b3,b4,b5)
asteroids_group.add(b1)
asteroids_group.add(b2)
asteroids_group.add(b3)
asteroids_group.add(b4)
asteroids_group.add(b5)
pygame.time.set_timer(pygame.USEREVENT, 100)
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
    collision = pygame.sprite.spritecollide(sp, asteroids_group, False)
    for c in collision:
        finishGame("GAME OVER", screen)
        inGame = False
    if missile is not None:
        collisionMissile = pygame.sprite.spritecollide(missile, asteroids_group, False)
        for coll in collisionMissile:
            screen.blit(bk, (0, 0))
            screen.blit(destroyed_asteroids, coll.getRect())
            pygame.display.flip()
            asteroids_group.remove(coll)
    if len(list(asteroids_group)) == 0:
        finishGame("YOU WON", screen)
        inGame = False

    screen.blit(bk, (0, 0))
    if fire:
        missile.move()
        screen.blit(missileimg, missile.getRect())
    screen.blit(shuttle, sp.getRect())
    for x in asteroids_group:
        screen.blit(asteroid, x.getRect())


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
