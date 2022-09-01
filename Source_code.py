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
