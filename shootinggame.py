import pygame
pygame.init()
import random

screen_width= 800
screen_height= 600


screen= pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Shooting Game")

icon= pygame.image.load("Sunflower.jpg")
pygame.display.set_icon(icon)

#create player
player_img = pygame.image.load("/home/anwesha/Documents/Pythongame/player1.jpeg").convert()
playerX = 370
playerY = 480
playerX_change=0

#Create enemy
enemy_img = pygame.image.load("/home/anwesha/Documents/Pythongame/enemy.jpeg").convert()
enemyX = random.randint(0,736)
enemyY = random.randint(50,150)
enemyX_change = 5
enemyY_change = 30

#player function
def player(x, y):
    screen.blit(player_img,(x,y))

#enemy function
def enemy(x,y):
    screen.blit(enemy_img, (x,y))

#Game Loop
running = True
while running:
    screen.fill((125,125,125))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -10
            if event.key == pygame.K_RIGHT:
                playerX_change = 10
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
    enemyX += enemyX_change

    if enemyX <= 0:
        enemyX_change = 3
        enemyY += enemyY_change
    elif enemyX >= 736:
        enemyX_change = -3
        enemyY += enemyY_change


    player(playerX, playerY)
    enemy(enemyX, enemyY)
    #update the screen
    pygame.display.update()

    

    
    
    
pygame.quit()