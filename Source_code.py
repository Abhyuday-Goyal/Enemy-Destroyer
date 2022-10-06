import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))#800 is the x value and 600 is the y value
pygame.display.set_caption("Space Invaders")
playerimg = pygame.image.load("shooter.png")
playerX = 370
playerY = 480
playerX_change = 0
enemyimg = pygame.image.load("enemy.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 0
nemyimg = pygame.image.load("enemy.png")
nemyX = random.randint(0,800)
nemyY = random.randint(50,150)
nemyX_change = 0.3
nemyY_change = 0
emyimg = pygame.image.load("enemy.png")
emyX = random.randint(0,800)
emyY = random.randint(50,150)
emyX_change = 0.3
emyY_change = 0
myimg = pygame.image.load("enemy.png")
myX = random.randint(0,800)
myY = random.randint(50,150)
myX_change = 0.3
myY_change = 0
