#Arsen Cui
#ICS2O1
#Mr. Radulovic
#Culminating Activity - Space Shooter

import pygame
import random
import math
pygame.init()
length = 800 # Length of window
height = 600 # Height of window
window = pygame.display.set_mode((length,height))
pygame.display.set_caption('Space Shooter')

white = [255, 255, 255]

enemyx = [] # List that stores all of the x-positions of the enemies
enemyy = [] # List that stores all of the y-positions of the enemies
speed = [] # List that stores all of the speeds of the enemies (left or right)
speedlist = [-1, 1] # List storing the choices for the speeds (left or right)
enemymovetimer = 0 # Timer tracking the amount of time the enemy has moved
enemyspawntimer = 0 # Timer tracking the amount of time before spawning more enemies
enemy_increment = 1 # Amount to increase the number of enemies by every 5 seconds
enemyremovelist = [] # List storing all of the enemies that need to be removed

ship = pygame.image.load(r'C:\Users\IT LAB\mu_code\images\Spaceship.png') # The spaceship that the player controls
ship = pygame.transform.scale(ship, (50, 50))
enemy = pygame.image.load(r'C:\Users\IT LAB\mu_code\images\Enemy.png') # The enemies that the player have to kill
enemy = pygame.transform.scale(enemy, (50, 50))
background = pygame.image.load(r'C:\Users\IT LAB\mu_code\images\GameBG.png') # The background of the game
background = pygame.transform.scale(background, (800, 600))
osu = pygame.image.load(r'D:\game\OSU3.png') # The bullets that the spaceship shoots
osu = pygame.transform.scale(osu, (50, 50))

shipx = 375 # Ship x-position
shipy = 500 # Ship y-position

gameover = False # Variable tracking whether the game is over or not

pygame.key.set_repeat(1) # Allows you to hold down a button and have the program be able to do something continuously

bullets = [] # List storing all of the bullet positions
bullets2 = [] # Second list used when removing bullets from the game
bulletspeed = 8 # Speed of the bullets
bulletsremovelist = [] # List storing all of the bullets that need to be removed

shoottimer = 0 # Timer tracking what interval to shoot bullets at
scoretimer = 0 # Timer tracking what your current score is
finalscore = 0 # The score that will be displayed on the screen after the game is over
highscore = 0 # Time tracking what your highscore is
finalhighscore = 0 #The highest score you have achieved so far

shipdirection = 0 # Current direction ship is moving in
shoot = False # Variable tracking whether to shoot bullets or not

num_enemy = 3 # Amount of initial enemies

pygame.mouse.set_visible(False) # Makes the mouse invisible on the screen

font = pygame.font.SysFont("Times New Roman", 25)
displaytext = False # Variable tracking whether to display the score or not

def updateBullets(bullets): # Updates the positions of the bullets on the screen every frame
    for i in range(0, len(bullets)):
        bullets[i][1] -= bulletspeed

def drawBullets(window, bullets): # Draws the bullets
    global osu
    for i in range(0, len(bullets)):
        window.blit(osu, (bullets[i][0], bullets[i][1]))

def appendEnemy(num_enemy, enemyx, enemyy): # Appends enemy x and y positions to the lists
    for i in range(num_enemy):
        enemyx.append(random.randint(0, length - 50))
        enemyy.append(random.randint(0, height - 500))

def drawEnemy(window, enemyx, enemyy): # Draws the enemies
    for i in range(num_enemy):
        window.blit(enemy, (enemyx[i], enemyy[i]))

def moveEnemysideways(num_enemy, speed, enemyx): # Moves the enemies sideways
    for i in range(num_enemy):
        speed.append(random.choice(speedlist))
        if speed[i] <= 0: # If the enemy speed is currently negative
            enemyx[i] += speed[i] # Move the enemy to the left
            if enemyx[i] <= 0: # If the enemy has touched the left side of the screen
                speed[i] = -speed[i] # Change the enemy's direction to move to the right
        elif speed[i] >= 0: # If the enemy speed is currently positive
            enemyx[i] += speed[i] # Move the enemy to the right
            if enemyx[i] >= length - 50: # If the enemy has touched the right side of the screen
                speed[i] = -speed[i] # Change the enemy's direction to move to the left

def moveEnemyforward(num_enemy, enemyy): # Moves the enemies forward
    for i in range(num_enemy):
        enemyy[i] += 1

def StartOver(num_enemy): # Restarts the game (Clear all lists, append new positions and speeds for the enemies)
    list.clear(enemyx)
    list.clear(enemyy)
    list.clear(speed)
    list.clear(bulletsremovelist)
    list.clear(enemyremovelist)
    list.clear(bullets)
    for i in range(num_enemy):
        enemyx.append(random.randint(0, length - 50))
        enemyy.append(random.randint(0, height - 500))
        speed.append(random.choice(speedlist))

appendEnemy(num_enemy, enemyx, enemyy) # Appends positions and speeds for the initial 3 enemies at the start

clock = pygame.time.Clock()
quit = False
while not quit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                shipdirection = "up"
            if event.key == pygame.K_DOWN:
                shipdirection = "down"
            if event.key == pygame.K_RIGHT:
                shipdirection = "right"
            if event.key == pygame.K_LEFT:
                shipdirection = "left"
            if event.key == pygame.K_SPACE:
                shoot = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                shoot = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(num_enemy):
                if event.button == 1:
                    if gameover == True: # If the game is over
                        StartOver(3) # Restart the game, and reset all the timers and variables
                        enemymovetimer = 0
                        enemyspawntimer = 0
                        shoottimer = 0
                        scoretimer = 0
                        enemy_increment = 1
                        num_enemy = 3
                        displaytext = False
                        shoot = False
                        gameover = False

    # If the ship has reached the edges of the screen, stop it from moving any further
    if shipx > length - 55:
        shipx = length - 55
    if shipx < 0:
        shipx = 0
    if shipy > height - 55:
        shipy = height - 55
    if shipy < 0:
        shipy = 0

    window.blit(background, (0,0)) # Draws the background
    window.blit(ship, (shipx, shipy)) # Draws the ship

    # Moves the ship in the specified directions
    if shipdirection == "up":
        shipy -= 5
    if shipdirection == "down":
        shipy += 5
    if shipdirection == "right":
        shipx += 5
    if shipdirection == "left":
        shipx -= 5

    # Sets initial x and y positions for the bullets
    bulletx = shipx + 2
    bullety = shipy - 35

    drawEnemy(window, enemyx, enemyy) # Draws the enemies

    if shoot == True: # If the signal has been given to shoot
        shoottimer += 1
        if shoottimer >= 20: # Every third of a second, shoot a bullet
            bullets.append([bulletx, bullety]) # Appends position for bullet
            shoottimer = 0 # Resets the shoot timer

        for i in range(len(bullets)):
            if bullets[i][1] > -20: # If the bullet has not gone past the top of the screen
                bullets2.append(bullets[i]) # Append that bullet to the second bullet list
        bullets = bullets2 # Removes all bullets that went through the top of the screen
        bullets2 = [] # Empties the list

    drawBullets(window, bullets) # Draws the bullets
    updateBullets(bullets) # Updates the bullets' positions

    for j in range(0, len(enemyx)):
        for i in range(0, len(bullets)):
            if bullets[i][0] <= enemyx[j] + 50 and bullets[i][0] >= enemyx[j] - 30 and bullets[i][1] <= enemyy[j] + 50 \
                    and bullets[i][1] >= enemyy[j]: # If a bullet has hit an enemy

                explosion.play() # Makes explosion noise

                if i in bulletsremovelist: # If the bullet has already been appended to the remove list
                    pass # Don't append it
                elif i not in bulletsremovelist: # If the bullet has not yet been appended to the remove list
                    bulletsremovelist.append(i) # Append the bullet to the remove list

                if j in enemyremovelist: # If the enemy has already been appended to the remove list
                    pass # Don't append it
                elif j not in enemyremovelist: # If the enemy has not yet been appended to the remove list
                    enemyremovelist.append(j) # Append the enemy to the remove list

    if len(bulletsremovelist) > 0: # If there are bullets in the bullet remove list
        for i in range(len(bulletsremovelist)):
            bullets.pop(bulletsremovelist[i]) # Remove those bullets from the bullets list
        bulletsremovelist = [] # Empty the list

    if len(enemyremovelist) > 0: # If there are enemies in the enemy remove list
        for i in range(len(enemyremovelist)):
            # Remove the enemies from the position and speed lists
            enemyx.pop(enemyremovelist[i])
            enemyy.pop(enemyremovelist[i])
            speed.pop(enemyremovelist[i])
            num_enemy = len(enemyx) # Updates the amount of enemies
        enemyremovelist = [] # Empty the list

    enemymovetimer += 1 # Increment the amount of time that has passed to track when to move the enemy

    if enemymovetimer >= 1:
        if enemymovetimer <= 180: # In the first 3 seconds
            moveEnemysideways(num_enemy, speed, enemyx) # Move the enemies sideways

        if enemymovetimer >= 181: # After 3 seconds
            moveEnemyforward(num_enemy, enemyy) # Move the enemies forward
            if enemymovetimer >= 360: # After another 3 seconds
                enemymovetimer = 0 # Restart the timer

    enemyspawntimer += 1 # Increment the amount of time that has passed before adding more enemies

    if enemyspawntimer >= 300: # If 5 seconds have passed
        # Append more enemies
        num_enemy += enemy_increment
        appendEnemy(enemy_increment, enemyx, enemyy)
        enemy_increment += 1 # Increase the amount of enemies to be appended every time
        num_enemy = len(enemyx) # Update the amount of enemies
        enemyspawntimer = 0 # Restart the timer

    if displaytext == False: # If the score has not yet been displayed
        scoretimer += 1 # Update the current score

    for i in range(num_enemy):
        if enemyy[i] >= height - 50: # If the enemy has gone past the bottom of the screen
            for i in range(num_enemy):
                speed[i] = 0 # Stop all the enemies from moving
                enemyx[i] = 1000 # Move all the existing enemies off the screen, "deleting" them
            displaytext = True # Display the score
            if scoretimer > highscore: # If the current score is better than your highscore
                # Set the current score to the new highscore
                finalhighscore = math.floor(scoretimer / 60)
                highscore = scoretimer
            finalscore = math.floor(scoretimer / 60)  # This is the score converted to seconds

    if displaytext == True: # If the signal has been given to display the score
        score = font.render(("Score: " + str(finalscore) + " Seconds"), 1, white)
        window.blit(score, (50, 200))  # Displays score
        highscorelabel = font.render(("Highscore: " + str(finalhighscore) + " Seconds"), 1, white)
        window.blit(highscorelabel, (50, 250)) # Displays highscore
        label = font.render("Click anywhere on the screen to play again", 1, white)
        window.blit(label, (50, 300)) #Displays instructions to restart the game
        gameover = True # The game is over

    pygame.display.update()
    clock.tick(60)

pygame.quit()