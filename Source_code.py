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
enemyimg = []
enemyX =[]
enemyY = []
enemyX_change =[]
enemyY_change =[]
num = 6
for i in range(num):
    enemyimg.append(pygame.image.load("enemy.png"))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(0.3)
    enemyY_change.append(40)


#bullet
# Ready: bullet not visible
# fire: bullet visible
bulletimg = pygame.image.load("img_3.png")
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 5
bullet_state = 'ready'
#score
score_val = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10
#text for game over
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x,y):
    score = font.render('score: '+ str(score_val), True, (255,255,255))
    screen.blit(score,(x,y))
def game_over():
    over_score = over_font.render('Game Over' , True, (255, 255, 255))
    screen.blit(over_score,(200,250))
def player(x,y):
    screen.blit(playerimg,(x,y))# we assign the img the x and y coordinates
def enemy(x,y,i):
    screen.blit(enemyimg[i],(x,y))# we assign the img the x and y coordinates
def fire_bullet(x,y):
    global bullet_state  # using global to access value of bullet state given outside the function
    bullet_state = 'fire'
    screen.blit(bulletimg,(x+16,y+10)) # x + 16 and y+ 10 to make sure bullet fires from the centre if spaceship
def isCollision(enemyX,enemyY,bulletX,bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
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

    for i in range(num):
        #game over code:
        if enemyY[i]>480:
            for j in range(num):
                enemyY[j] = 2000
            game_over()
            break
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
# for collisions
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_val += 1
            print(score_val)
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i],i)

    #bullet movement
    if bulletY <= 0:
        bulletY = 400
        bullet_state = 'ready'
    if bullet_state is 'fire':
        fire_bullet(bulletX,bulletY)
        bulletY -= bulletY_change
    player(playerX, playerY)
    show_score(textX,textY)
    pygame.display.update()  # to keep updating the game




