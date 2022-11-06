import pygame
import random
import math
pygame.init()
screen = pygame.display.set_mode((800,600))#800 is the x value and 600 is the y value
pygame.display.set_caption("Space Invaders")
playerimg = pygame.image.load("shooter.png")
playerX = 370
playerY = 480
playerX_change = 0
#enemy
enemyimg = pygame.image.load("enemy.png")
enemyX = random.randint(0,735)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40

#bullet
# Ready: bullet not visible
# fire: bullet visible
bulletimg = pygame.image.load("img_3.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'
score = 0
def player(x,y):
    screen.blit(playerimg,(x,y))# we assign the img the x and y coordinates
def enemy(x,y):
    screen.blit(enemyimg,(x,y))# we assign the img the x and y coordinates
def fire_bullet(x,y):
    global bullet_state  # using global to access value of bullet state given outside the function
    bullet_state = 'fire'
    screen.blit(bulletimg,(x+16,y+10)) # x + 16 and y+ 10 to make sure bullet fires from the centre if spaceship
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletY,2))+ (math.pow(enemyY-bulletY,2)))
    if distance<27:
        return True
    else:
        return False


run = True
while run:
    screen.fill((255, 0, 0))  # for colour of screen( still in the while loop running continously)
    for i in pygame.event.get(): # to go through all the events happening in the game
        if i.type == pygame.QUIT:
            run = False
        if i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                playerX_change -= 0.5
                #print("Left arrow is pressed ")
            if i.key == pygame.K_RIGHT:
                playerX_change += 0.5
                #print("Right arrow is pressed")
            if i.key == pygame.K_SPACE:
                if bullet_state is 'ready':
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        if i.type == pygame.KEYUP:
            if i.key == pygame.K_LEFT or i.key == pygame.K_RIGHT:
                playerX_change = 0#So that when we release the key, it stops
                #print("Arrow key has been released")
    playerX += playerX_change
    if playerX<= 0:
        playerX=0
    elif playerX>= 736:
        playerX = 736
    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 1
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -1
        enemyY += enemyY_change

#bullet movement
    if bulletY <= 0:
        bulletY = 400
        bullet_state = 'ready'
        score += 1
        print(score)
        enemyX = random.randint(0, 735)
        enemyY = random.randint(50, 150)

    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
#for collisions
    collision = isCollision(enemyX,enemyY,bulletX,bulletY)
    if collision:
        bulletY = 480
        bullet_state = 'ready'
    player(playerX, playerY)
    enemy(enemyX,enemyY)
    pygame.display.update()  # to keep updating the game
