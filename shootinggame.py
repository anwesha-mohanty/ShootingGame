import pygame
pygame.init()
import random
import math
from pygame import mixer

screen_width= 800
screen_height= 600


screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Shooting Game")

icon= pygame.image.load("gameicon.jpg")
pygame.display.set_icon(icon)
#setting background image
background = pygame.image.load("bgImage.jpg").convert()

#create player
player_img = pygame.image.load("player.jpg").convert()
playerX = 370
playerY = 480
playerX_change=0

#Enemies
enemy_img =[]
enemyX = []
enemyY = []
enemyX_change =  []
enemyY_change = []
num_of_enemies = 6

#Create enemy
for i in range(num_of_enemies):
    enemy_img.append(pygame.image.load("enemy.jpg").convert())
    enemyX.append(random.randint(0,736))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2) 
    enemyY_change.append(40)

#create bullet
bullet_img = pygame.image.load("bullet.jpg")
bulletX=0
bulletY=480
bulletX_change = 0
bulletY_change = 5
bullet_state = "ready"

#Score
score_value = 0
font = pygame.font.Font("freesansbold.ttf",32)
textX = 10
textY = 10  

#Background music
mixer.music.load("bgmusic.ogg")
mixer.music.play(-1)

#Game Over text
game_over_font = pygame.font.Font("freesansbold.ttf", 55)


#player function
def player(x, y):
    screen.blit(player_img,(x,y))

#enemy function
def enemy(x,y):
    screen.blit(enemy_img[i], (x,y))

#bullet function
def fire_bullet(x,y):
    global bullet_state
    bullet_state ="fire"
    screen.blit(bullet_img,(x,y))

#display score
def show_score(x,y):
    score = font.render("Score: "+ str(score_value), True, (0,0,0))
    screen.blit(score, (x,y))


#Collision detection
def isCollision(enemyX,enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2))+(math.pow(enemyY-bulletY,2)))

    #collision detected
    if distance < 26:
        return True
    else:
        return False

#Game over text
def game_over_text():
    game_over_msg = game_over_font.render("GAME OVER!", True, (0,0,0))
    screen.blit(game_over_msg,(200,250))


#GAME LOOP

running = True
while running:
    screen.fill((0,0,0))
    screen.blit(background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        #player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
            
            #for firing bullet press space bar
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    gunshot = mixer.Sound("gunshot.ogg")
                    gunshot.play()
                    bulletX = playerX
                    fire_bullet(bulletX,bulletY)
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change =0
        playerX += playerX_change
        #Adding boundaries so player doesn't go off screen
        if playerX <= 0:
            playerX = 0
        elif playerX >= 736:
            playerX = 736
        
    
    #enemy movement
    for i in range(num_of_enemies):
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
        
        #Game over condition
        if enemyY[i] > 450:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
    
        #collision detection code
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound("explosion.ogg")
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            
            #respawn the enemy
            enemyX[i] = random.randint(0,736)
            enemyY[i]= random.randint(50,150)
        enemy(enemyX[i], enemyY[i])

    
    #bullet movement
    if bulletY <= 0:
        bulletY = 480
        bullet_state = "ready"

    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    show_score(textX,textY)
    
    #update the screen
    pygame.display.update()

pygame.quit()