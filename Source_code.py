import pygame
import random
pygame.init()
screen = pygame.display.set_mode((800,600))#800 is the x value and 600 is the y value
pygame.display.set_caption("Space Invaders")
playerimg = pygame.image.load("shooter.png")
playerX = 370
playerY = 480
playerX_change = 0
#enemies
enemyimg = pygame.image.load("enemy.png")
enemyX = random.randint(0,800)
enemyY = random.randint(50,150)
enemyX_change = 0.3
enemyY_change = 40
nemyimg = pygame.image.load("enemy.png")
nemyX = random.randint(0,800)
nemyY = random.randint(50,150)
nemyX_change = 0.3
nemyY_change = 40
emyimg = pygame.image.load("enemy.png")
emyX = random.randint(0,800)
emyY = random.randint(50,150)
emyX_change = 0.3
emyY_change = 40
myimg = pygame.image.load("enemy.png")
myX = random.randint(0,800)
myY = random.randint(50,150)
myX_change = 0.3
myY_change = 40
#bullet
# Ready: bullet not visible
# fire: bullet visible
bulletimg = pygame.image.load("img_3.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 40
bullet_state = 'ready'
def player(x,y):
    screen.blit(playerimg,(x,y))# we assign the img the x and y coordinates
def enemy(x,y):
    screen.blit(enemyimg,(x,y))# we assign the img the x and y coordinates
def nemy(x,y):
    screen.blit(nemyimg,(x,y))
def emy(x,y):
    screen.blit(emyimg,(x,y))
def my(x,y):
    screen.blit(myimg, (x, y))
def fire_bullet(x,y):
    global bullet_state  # using global to acess value of bullet state given outside the function 
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
    nemyX += nemyX_change
    if nemyX <= 0:
        nemyX_change = 1
        nemyY += nemyY_change
    elif nemyX >= 736:
        nemyX_change = -1
        nemyY += nemyY_change
    emyX += emyX_change
    if emyX <= 0:
        emyX_change = 1
        emyY += emyY_change
    elif emyX >= 736:
        emyX_change = -1
        emyY += emyY_change
    myX += myX_change
    if myX <= 0:
        myX_change = 1
        myY += myY_change
    elif myX >= 736:
        myX_change = -1
        myY += myY_change
    player(playerX, playerY)
    enemy(enemyX,enemyY)
    nemy(nemyX,nemyY)
    emy(emyX,emyY)
    my(myX,myY)
    pygame.display.update()  # to keep updating the game
