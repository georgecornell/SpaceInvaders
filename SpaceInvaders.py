#I have no doubt that there is a better way to do this, probably with OOP. But by the time it occured to me to do that, I was too far into development for it to be worth changing.
import sys
import platform
import os
try:
    import pygame
    import pygame.mixer
    from pygame.locals import *
except ImportError:
    print("You have not installed Pygame. This game cannot run without Pygame. Please install it, and try again.")
    if platform.system() == "Windows":
        if sys.version[0] == "3":
            goto = input("Would you like to go to the Pygame download page in your default browser? (y/n)")
        else:
            goto = raw_input("Would you like to go to the Pygame download page in your default browser? (y/n)")
        if goto.lower() == "y":
            os.system("start http://pygame.org/download.shtml")
    sys.exit()#Yes, I know sys.exit() is bad practice. But I can't be bothered to put the entire program under an if/else statement. Even if sys.exit() fails, the program will crash.
from random import randrange as rand
from math import floor

folder = sys.path[0]
if platform.system() == "Windows":
    folder += "\\"
else:
    folder += "/"
pygame.init()

pygame.display.set_caption("Space Invaders")

size = width, height = 800,400
screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()

playershot = pygame.mixer.Sound(folder + 'playershot.wav')
enemyshot = pygame.mixer.Sound(folder + 'enemyshot.wav')
playerexplode = pygame.mixer.Sound(folder + 'explode.wav')
gameover = pygame.mixer.Sound(folder + 'gameover.wav')

#****************************************

gameState = "start"

mouseIsPressed = False

px = 385
lives = 3
death = 0
completeTimer = 0
gameOverTimer = 200
moving = 0
shooting = False
pbxy = [400, 600] #Using a list for the position is necessary for everything to work correctly. (See the "enemy" function, near the end.)

score = [0] #Here, too.

prect = pygame.Rect(px, 385, 30, 15)
prect2 = pygame.Rect(px+8, 370, 14, 15)
playSur = pygame.Surface(size)

enemies = [
    [1, 1, 1, 1, 1, 1],
    [2, 2, 2, 2, 2, 2],
    [3, 3, 3, 3, 3, 3],
    [4, 4, 4, 4, 4, 4],
    [5, 5, 5, 5, 5, 5],
    [6, 6, 6, 6, 6, 6]
]
speed = 2
estate = 1
ex = 20
ey = 10
wentDown = False
edirection = "right"
updateTicks = 0
ebx = []
eby = []

def drawPixel(posx, posy):
    pygame.draw.rect(playSur, (255, 255, 255), pygame.Rect(posx, posy, 4, 3))

def enemy(posx, posy, vx, vy):
    #Width: 32px Height: 30px
    #Enemy 1:
    if estate == 0 and enemies[vy][vx] == 1:
        drawPixel(posx, posy)
        drawPixel(posx+4, posy+3)
        drawPixel(posx+8, posy+6)
        drawPixel(posx+12, posy+9)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+20, posy+6)
        drawPixel(posx+24, posy+3)
        drawPixel(posx+28, posy+6)
        drawPixel(posx+28, posy+9)
        
        drawPixel(posx+4, posy+12)
        drawPixel(posx+8, posy+12)
        drawPixel(posx+12, posy+12)
        drawPixel(posx+16, posy+12)
        drawPixel(posx+20, posy+12)

        drawPixel(posx+4, posy+15)
        drawPixel(posx+12, posy+15)
        drawPixel(posx+20, posy+15)
        drawPixel(posx+24, posy+15)

        drawPixel(posx+4, posy+18)
        drawPixel(posx+8, posy+18)
        drawPixel(posx+12, posy+18)
        drawPixel(posx+16, posy+18)
        drawPixel(posx+20, posy+18)
        drawPixel(posx+24, posy+18)

        drawPixel(posx+4, posy+21)
        drawPixel(posx+8, posy+21)
        drawPixel(posx+12, posy+21)
        drawPixel(posx+16, posy+21)
        drawPixel(posx+20, posy+21)
        drawPixel(posx+24, posy+21)

        drawPixel(posx+4, posy+24)
        drawPixel(posx+24, posy+24)
        drawPixel(posx, posy+27)
        drawPixel(posx+4, posy+27)
        drawPixel(posx+20, posy+27)
        drawPixel(posx+24, posy+27)

    if estate == 1 and enemies[vy][vx] == 1:
        drawPixel(posx+28, posy)
        drawPixel(posx+24, posy+3)
        drawPixel(posx+20, posy+6)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+12, posy+9)
        drawPixel(posx+8, posy+6)
        drawPixel(posx+4, posy+3)
        drawPixel(posx, posy+6)
        drawPixel(posx, posy+9)
        
        drawPixel(posx+8, posy+12)
        drawPixel(posx+12, posy+12)
        drawPixel(posx+16, posy+12)
        drawPixel(posx+20, posy+12)
        drawPixel(posx+24, posy+12)

        drawPixel(posx+4, posy+15)
        drawPixel(posx+8, posy+15)
        drawPixel(posx+16, posy+15)
        drawPixel(posx+24, posy+15)
        drawPixel(posx+28, posy+15)

        drawPixel(posx+4, posy+18)
        drawPixel(posx+8, posy+18)
        drawPixel(posx+12, posy+18)
        drawPixel(posx+16, posy+18)
        drawPixel(posx+20, posy+18)
        drawPixel(posx+24, posy+18)

        drawPixel(posx+4, posy+21)
        drawPixel(posx+8, posy+21)
        drawPixel(posx+12, posy+21)
        drawPixel(posx+16, posy+21)
        drawPixel(posx+20, posy+21)
        drawPixel(posx+24, posy+21)

        drawPixel(posx+4, posy+24)
        drawPixel(posx+24, posy+24)
        drawPixel(posx, posy+27)
        drawPixel(posx+4, posy+27)
        drawPixel(posx+8, posy+27)
        drawPixel(posx+20, posy+27)
        drawPixel(posx+24, posy+27)
        drawPixel(posx+28, posy+27)

    #Enemy 2:
    if estate == 0 and enemies[vy][vx] == 2:
        drawPixel(posx+8, posy)
        drawPixel(posx+12, posy)
        drawPixel(posx+16, posy)
        drawPixel(posx+20, posy)

        drawPixel(posx+4, posy+3)
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+24, posy+3)

        drawPixel(posx, posy+6)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+8, posy+6)
        drawPixel(posx+12, posy+6)
        drawPixel(posx+16, posy+6)
        drawPixel(posx+20, posy+6)
        drawPixel(posx+24, posy+6)
        drawPixel(posx+28, posy+6)

        drawPixel(posx, posy+9)
        drawPixel(posx+8, posy+9)
        drawPixel(posx+20, posy+9)
        drawPixel(posx+28, posy+9)

        drawPixel(posx+4, posy+12)
        drawPixel(posx+12, posy+12)
        drawPixel(posx+16, posy+12)
        drawPixel(posx+24, posy+12)
        drawPixel(posx+4, posy+15)
        drawPixel(posx+12, posy+15)
        drawPixel(posx+16, posy+15)
        drawPixel(posx+24, posy+15)
        drawPixel(posx+4, posy+18)
        drawPixel(posx+12, posy+18)
        drawPixel(posx+16, posy+18)
        drawPixel(posx+24, posy+18)

    if estate == 1 and enemies[vy][vx] == 2:
        drawPixel(posx+8, posy)
        drawPixel(posx+12, posy)
        drawPixel(posx+16, posy)
        drawPixel(posx+20, posy)

        drawPixel(posx+4, posy+3)
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+24, posy+3)

        drawPixel(posx, posy+6)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+8, posy+6)
        drawPixel(posx+12, posy+6)
        drawPixel(posx+16, posy+6)
        drawPixel(posx+20, posy+6)
        drawPixel(posx+24, posy+6)
        drawPixel(posx+28, posy+6)

        drawPixel(posx, posy+9)
        drawPixel(posx+8, posy+9)
        drawPixel(posx+20, posy+9)
        drawPixel(posx+28, posy+9)
        drawPixel(posx, posy+12)
        drawPixel(posx+12, posy+12)
        drawPixel(posx+16, posy+12)
        drawPixel(posx+28, posy+12)
        drawPixel(posx, posy+15)
        drawPixel(posx+8, posy+15)
        drawPixel(posx+20, posy+15)
        drawPixel(posx+28, posy+15)
        drawPixel(posx, posy+18)
        drawPixel(posx+8, posy+18)
        drawPixel(posx+20, posy+18)
        drawPixel(posx+28, posy+18)

    #Enemy 3:
    if estate == 0 and enemies[vy][vx] == 3:
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+12, posy+6)
        drawPixel(posx+16, posy+6)
        drawPixel(posx+24, posy+6)

        drawPixel(posx, posy+9)
        drawPixel(posx+8, posy+9)
        drawPixel(posx+12, posy+9)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+20, posy+9)
        drawPixel(posx+28, posy+9)

        drawPixel(posx, posy+12)
        drawPixel(posx+12, posy+12)
        drawPixel(posx+16, posy+12)
        drawPixel(posx+28, posy+12)

        drawPixel(posx+8, posy+15)
        drawPixel(posx+20, posy+15)
        drawPixel(posx+4, posy+18)
        drawPixel(posx+24, posy+18)
        drawPixel(posx+8, posy+21)
        drawPixel(posx+20, posy+21)

    if estate == 1 and enemies[vy][vx] == 3:
        drawPixel(posx, posy)
        drawPixel(posx+28, posy)
        drawPixel(posx, posy+3)
        drawPixel(posx+8, posy+3)
        drawPixel(posx+20, posy+3)
        drawPixel(posx+28, posy+3)

        drawPixel(posx+4, posy+6)
        drawPixel(posx+12, posy+6)
        drawPixel(posx+16, posy+6)
        drawPixel(posx+24, posy+6)

        drawPixel(posx+12, posy+9)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+12, posy+12)
        drawPixel(posx+16, posy+12)

        drawPixel(posx+8, posy+15)
        drawPixel(posx+20, posy+15)
        drawPixel(posx, posy+18)
        drawPixel(posx+4, posy+18)
        drawPixel(posx+24, posy+18)
        drawPixel(posx+28, posy+18)

    #Enemy 4:
    if estate == 0 and enemies[vy][vx] == 4:
        drawPixel(posx+8, posy)
        drawPixel(posx+12, posy)
        drawPixel(posx+16, posy)
        drawPixel(posx+20, posy)
        drawPixel(posx+4, posy+3)
        drawPixel(posx+8, posy+3)
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+20, posy+3)
        drawPixel(posx+24, posy+3)

        drawPixel(posx, posy+6)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+12, posy+6)
        drawPixel(posx+20, posy+6)
        drawPixel(posx+24, posy+6)
        drawPixel(posx+28, posy+6)

        drawPixel(posx+4, posy+9)
        drawPixel(posx+8, posy+9)
        drawPixel(posx+12, posy+9)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+20, posy+9)
        drawPixel(posx+24, posy+9)
        
        drawPixel(posx+8, posy+12)
        drawPixel(posx+20, posy+12)
        drawPixel(posx+4, posy+15)
        drawPixel(posx+24, posy+15)

        drawPixel(posx+8, posy+18)
        drawPixel(posx+12, posy+18)
        drawPixel(posx+16, posy+18)
        drawPixel(posx+20, posy+18)

    if estate == 1 and enemies[vy][vx] == 4:
        drawPixel(posx+8, posy)
        drawPixel(posx+12, posy)
        drawPixel(posx+16, posy)
        drawPixel(posx+20, posy)
        drawPixel(posx+4, posy+3)
        drawPixel(posx+8, posy+3)
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+20, posy+3)
        drawPixel(posx+24, posy+3)

        drawPixel(posx, posy+6)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+8, posy+6)
        drawPixel(posx+16, posy+6)
        drawPixel(posx+24, posy+6)
        drawPixel(posx+28, posy+6)

        drawPixel(posx+4, posy+9)
        drawPixel(posx+8, posy+9)
        drawPixel(posx+12, posy+9)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+20, posy+9)
        drawPixel(posx+24, posy+9)

        drawPixel(posx+8, posy+12)
        drawPixel(posx+20, posy+12)
        drawPixel(posx+8, posy+15)
        drawPixel(posx+20, posy+15)
        drawPixel(posx+4, posy+18)
        drawPixel(posx+24, posy+18)
        drawPixel(posx, posy+21)
        drawPixel(posx+28, posy+21)

    #Enemy 5
    if estate == 0 and enemies[vy][vx] == 5:
        drawPixel(posx+8, posy)
        drawPixel(posx+12, posy)
        drawPixel(posx+16, posy)
        drawPixel(posx+20, posy)
        drawPixel(posx+4, posy+3)
        drawPixel(posx+8, posy+3)
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+20, posy+3)
        drawPixel(posx+24, posy+3)

        drawPixel(posx, posy+6)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+16, posy+6)
        drawPixel(posx+20, posy+6)
        drawPixel(posx+24, posy+6)
        drawPixel(posx+28, posy+6)
        drawPixel(posx, posy+9)
        drawPixel(posx+4, posy+9)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+20, posy+9)
        drawPixel(posx+24, posy+9)
        drawPixel(posx+28, posy+9)
        drawPixel(posx, posy+12)
        drawPixel(posx+4, posy+12)
        drawPixel(posx+8, posy+12)
        drawPixel(posx+12, posy+12)
        drawPixel(posx+16, posy+12)
        drawPixel(posx+20, posy+12)
        drawPixel(posx+24, posy+12)
        drawPixel(posx+28, posy+12)

        drawPixel(posx+8, posy+15)
        drawPixel(posx+12, posy+15)
        drawPixel(posx+16, posy+15)
        drawPixel(posx+24, posy+15)
        drawPixel(posx+8, posy+18)
        drawPixel(posx+24, posy+18)
        drawPixel(posx+8, posy+21)
        drawPixel(posx+24, posy+21)
        drawPixel(posx, posy+24)
        drawPixel(posx+4, posy+24)
        drawPixel(posx+8, posy+24)
        drawPixel(posx+16, posy+24)
        drawPixel(posx+20, posy+24)
        drawPixel(posx+24, posy+24)

    if estate == 1 and enemies[vy][vx] == 5:
        drawPixel(posx+8, posy)
        drawPixel(posx+12, posy)
        drawPixel(posx+16, posy)
        drawPixel(posx+20, posy)
        drawPixel(posx+4, posy+3)
        drawPixel(posx+8, posy+3)
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+20, posy+3)
        drawPixel(posx+24, posy+3)

        drawPixel(posx, posy+6)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+8, posy+6)
        drawPixel(posx+12, posy+6)
        drawPixel(posx+24, posy+6)
        drawPixel(posx+28, posy+6)
        drawPixel(posx, posy+9)
        drawPixel(posx+4, posy+9)
        drawPixel(posx+8, posy+9)
        drawPixel(posx+12, posy+9)
        drawPixel(posx+24, posy+9)
        drawPixel(posx+28, posy+9)
        drawPixel(posx, posy+12)
        drawPixel(posx+4, posy+12)
        drawPixel(posx+8, posy+12)
        drawPixel(posx+12, posy+12)
        drawPixel(posx+16, posy+12)
        drawPixel(posx+20, posy+12)
        drawPixel(posx+24, posy+12)
        drawPixel(posx+28, posy+12)

        drawPixel(posx+4, posy+15)
        drawPixel(posx+12, posy+15)
        drawPixel(posx+16, posy+15)
        drawPixel(posx+20, posy+15)
        drawPixel(posx+4, posy+18)
        drawPixel(posx+20, posy+18)
        drawPixel(posx+4, posy+21)
        drawPixel(posx+20, posy+21)
        drawPixel(posx+4, posy+24)
        drawPixel(posx+8, posy+24)
        drawPixel(posx+12, posy+24)
        drawPixel(posx+20, posy+24)
        drawPixel(posx+24, posy+24)
        drawPixel(posx+28, posy+24)

    #Enemy 6
    if estate == 0 and enemies[vy][vx] == 6:
        drawPixel(posx+12, posy)
        drawPixel(posx+16, posy)
        drawPixel(posx+4, posy+3)
        drawPixel(posx+8, posy+3)
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+20, posy+3)
        drawPixel(posx+24, posy+3)

        drawPixel(posx, posy+6)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+12, posy+6)
        drawPixel(posx+16, posy+6)
        drawPixel(posx+24, posy+6)
        drawPixel(posx+28, posy+6)
        
        drawPixel(posx, posy+9)
        drawPixel(posx+4, posy+9)
        drawPixel(posx+8, posy+9)
        drawPixel(posx+12, posy+9)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+20, posy+9)
        drawPixel(posx+24, posy+9)
        drawPixel(posx+28, posy+9)

        drawPixel(posx+4, posy+12)
        drawPixel(posx+24, posy+12)
        drawPixel(posx+4, posy+15)
        drawPixel(posx+24, posy+15)
        drawPixel(posx+8, posy+18)
        drawPixel(posx+24, posy+18)
        drawPixel(posx+12, posy+21)
        drawPixel(posx+28, posy+21)
        drawPixel(posx+16, posy+24)
        drawPixel(posx+28, posy+24)

    if estate == 1 and enemies[vy][vx] == 6:
        drawPixel(posx+12, posy)
        drawPixel(posx+16, posy)
        drawPixel(posx+4, posy+3)
        drawPixel(posx+12, posy+3)
        drawPixel(posx+16, posy+3)
        drawPixel(posx+24, posy+3)

        drawPixel(posx, posy+6)
        drawPixel(posx+4, posy+6)
        drawPixel(posx+12, posy+6)
        drawPixel(posx+16, posy+6)
        drawPixel(posx+24, posy+6)
        drawPixel(posx+28, posy+6)
        
        drawPixel(posx, posy+9)
        drawPixel(posx+4, posy+9)
        drawPixel(posx+8, posy+9)
        drawPixel(posx+12, posy+9)
        drawPixel(posx+16, posy+9)
        drawPixel(posx+20, posy+9)
        drawPixel(posx+24, posy+9)
        drawPixel(posx+28, posy+9)

        drawPixel(posx+4, posy+12)
        drawPixel(posx+24, posy+12)
        drawPixel(posx+4, posy+15)
        drawPixel(posx+24, posy+15)
        drawPixel(posx+4, posy+18)
        drawPixel(posx+20, posy+18)
        drawPixel(posx, posy+21)
        drawPixel(posx+16, posy+21)
        drawPixel(posx, posy+24)
        drawPixel(posx+12, posy+24)
    
    if pbxy[0] >= posx and pbxy[0] <= posx+32 and pbxy[1] >= posy and pbxy[1] <= posy+30:
        enemies[vy][vx] = 0
        pbxy[0] = 400
        pbxy[1] = 600

        score[0] += (7 - vy)*20

    elif posy >= 260 and posy <= 307 and enemies[vy][vx] != 0:
        if posx >= 150 and posx <= 217:
            for a in range(0, 6):
                theIndex = int(floor((posy-260)/7))
                boulder1[theIndex][a] = 0
                if theIndex > 0:
                    boulder1[theIndex-1][a] = 0
                if theIndex > 1:
                    boulder1[theIndex-2][a] = 0
        elif posx >= 350 and posx <= 417:
            for a in range(0, 6):
                theIndex = int(floor((posy-260)/7))
                boulder2[theIndex][a] = 0
                if theIndex > 0:
                    boulder2[theIndex-1][a] = 0
                if theIndex > 1:
                    boulder2[theIndex-2][a] = 0
        elif posx >= 550 and posx <= 617:
            for a in range(0, 6):
                theIndex = int(floor((posy-260)/7))
                boulder3[theIndex][a] = 0
                if theIndex > 0:
                    boulder3[theIndex-1][a] = 0
                if theIndex > 1:
                    boulder3[theIndex-2][a] = 0
    elif posy > 307 and enemies[vy][vx] != 0:
        if posx >= 150 and posx <= 217:
            for a in range(0, 6):
                boulder1[7][a] = 0
        elif posx >= 350 and posx <= 417:
            for a in range(0, 6):
                boulder2[7][a] = 0
        elif posx >= 550 and posx <= 617:
            for a in range(0, 6):
                boulder3[7][a] = 0

def newEB(x, y):
    ebx.append(x)
    eby.append(y)

def shoot():
    if not enemies == [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]:
        selectedCol = rand(0, 6)
        while enemies[5][selectedCol] == 0 and enemies[4][selectedCol] == 0 and enemies[3][selectedCol] == 0 and enemies[2][selectedCol] == 0 and enemies[1][selectedCol] == 0 and enemies[0][selectedCol] == 0:
            selectedCol = rand(0, 6)

        if not enemies[5][selectedCol] == 0:
            newEB(ex+(selectedCol*70)+16, ey+160)
        elif not enemies[4][selectedCol] == 0:
            newEB(ex+(selectedCol*70)+16, ey+135)
        elif not enemies[3][selectedCol] == 0:
            newEB(ex+(selectedCol*70)+16, ey+110)
        elif not enemies[2][selectedCol] == 0:
            newEB(ex+(selectedCol*70)+16, ey+85)
        elif not enemies[1][selectedCol] == 0:
            newEB(ex+(selectedCol*70)+16, ey+60)
        else:
            newEB(ex+(selectedCol*70)+16, ey+35)

UFOpos = 2400
UFOshot = False

def UFOpx(posx, posy):
    pygame.draw.rect(playSur, (150, 0, 200), pygame.Rect(posx, posy, 4, 3))

def drawUFO1():
    UFOpx(UFOpos+8, 20)
    UFOpx(UFOpos+12, 20)
    UFOpx(UFOpos+16, 20)
    UFOpx(UFOpos+4, 23)
    UFOpx(UFOpos+8, 23)
    UFOpx(UFOpos+12, 23)
    UFOpx(UFOpos+16, 23)
    UFOpx(UFOpos+20, 23)
    UFOpx(UFOpos, 26)
    UFOpx(UFOpos+4, 26)
    UFOpx(UFOpos+8, 26)
    UFOpx(UFOpos+12, 26)
    UFOpx(UFOpos+16, 26)
    UFOpx(UFOpos+20, 26)
    UFOpx(UFOpos+24, 26)

    UFOpx(UFOpos, 29)
    UFOpx(UFOpos+8, 29)
    UFOpx(UFOpos+16, 29)
    UFOpx(UFOpos+24, 29)

    UFOpx(UFOpos, 32)
    UFOpx(UFOpos+4, 32)
    UFOpx(UFOpos+8, 32)
    UFOpx(UFOpos+12, 32)
    UFOpx(UFOpos+16, 32)
    UFOpx(UFOpos+20, 32)
    UFOpx(UFOpos+24, 32)
    UFOpx(UFOpos+4, 35)
    UFOpx(UFOpos+8, 35)
    UFOpx(UFOpos+12, 35)
    UFOpx(UFOpos+16, 35)
    UFOpx(UFOpos+20, 35)
    UFOpx(UFOpos+8, 38)
    UFOpx(UFOpos+12, 38)
    UFOpx(UFOpos+16, 38)

def drawUFO2():
    UFOpx(UFOpos+8, 20)
    UFOpx(UFOpos+12, 20)
    UFOpx(UFOpos+16, 20)
    UFOpx(UFOpos+4, 23)
    UFOpx(UFOpos+8, 23)
    UFOpx(UFOpos+12, 23)
    UFOpx(UFOpos+16, 23)
    UFOpx(UFOpos+20, 23)
    UFOpx(UFOpos, 26)
    UFOpx(UFOpos+4, 26)
    UFOpx(UFOpos+8, 26)
    UFOpx(UFOpos+12, 26)
    UFOpx(UFOpos+16, 26)
    UFOpx(UFOpos+20, 26)
    UFOpx(UFOpos+24, 26)
    
    UFOpx(UFOpos, 29)
    UFOpx(UFOpos+4, 29)
    UFOpx(UFOpos+12, 29)
    UFOpx(UFOpos+20, 29)
    UFOpx(UFOpos+24, 29)

    UFOpx(UFOpos, 32)
    UFOpx(UFOpos+4, 32)
    UFOpx(UFOpos+8, 32)
    UFOpx(UFOpos+12, 32)
    UFOpx(UFOpos+16, 32)
    UFOpx(UFOpos+20, 32)
    UFOpx(UFOpos+24, 32)
    UFOpx(UFOpos+4, 35)
    UFOpx(UFOpos+8, 35)
    UFOpx(UFOpos+12, 35)
    UFOpx(UFOpos+16, 35)
    UFOpx(UFOpos+20, 35)
    UFOpx(UFOpos+8, 38)
    UFOpx(UFOpos+12, 38)
    UFOpx(UFOpos+16, 38)

boulder1 = [
[0, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1]
]
boulder2 = [
[0, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1]
]
boulder3 = [
[0, 0, 1, 1, 0, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[0, 1, 1, 1, 1, 0],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1],
[1, 1, 1, 1, 1, 1]
]

def boulderPixel(posx, posy, boulderInside, vx, vy):
    if boulderInside == 1 and boulder1[vy][vx] == 1:
        pygame.draw.rect(playSur, (220, 80, 0), pygame.Rect(posx, posy, 7, 7))
        if pbxy[0] >= posx and pbxy[0] <= posx+7 and pbxy[1] >= posy and pbxy[1] <= posy+7:
            boulder1[vy][vx] = 0
            pbxy[0] = 400
            pbxy[1] = 600
    if boulderInside == 2 and boulder2[vy][vx] == 1:
        pygame.draw.rect(playSur, (220, 80, 0), pygame.Rect(posx, posy, 7, 7))
        if pbxy[0] >= posx and pbxy[0] <= posx+7 and pbxy[1] >= posy and pbxy[1] <= posy+7:
            boulder2[vy][vx] = 0
            pbxy[0] = 400
            pbxy[1] = 600
    if boulderInside == 3 and boulder3[vy][vx] == 1:
        pygame.draw.rect(playSur, (220, 80, 0), pygame.Rect(posx, posy, 7, 7))
        if pbxy[0] >= posx and pbxy[0] <= posx+7 and pbxy[1] >= posy and pbxy[1] <= posy+7:
            boulder3[vy][vx] = 0
            pbxy[0] = 400
            pbxy[1] = 600

font = pygame.font.SysFont("Sans Serif, Arial, Times New Roman", 60)
SItext = font.render("Space Invaders", True, (255, 255, 255))
font = pygame.font.SysFont("Sans Serif, Arial, Times New Roman", 30)
playText = font.render("PLAY", True, (255, 255, 255))
textTimer = 0

font = pygame.font.SysFont("Sans Serif, Arial, Times New Roman", 80)
loseText = font.render("GAME OVER", True, (255, 255, 255))

font = pygame.font.SysFont("Sans Serif, Arial, Times New Roman", 150)
ThreeTwoOne3 = font.render("3", True, (255, 255, 255))
ThreeTwoOne2 = font.render("2", True, (255, 255, 255))
ThreeTwoOne1 = font.render("1", True, (255, 255, 255))

pygame.display.flip()

running = True

while running:
    clock.tick(30)
    mousePos = pygame.mouse.get_pos()
    mouseX = mousePos[0]
    mouseY = mousePos[1]
    
    if gameState == "start":
        textTimer += 1
        screen.fill((0, 0, 0))
        if textTimer % 2 == 0:
            screen.blit(SItext, (200, 75))
            screen.blit(playText, (365, 280))
        if mouseX >= 365 and mouseX <= 440 and mouseY >= 285 and mouseY <= 310 and mouseIsPressed == True:
            gameState = "playing"

    if gameState == "playing":
        prect = pygame.Rect(px, 385, 30, 15)
        prect2 = pygame.Rect(px+8, 370, 14, 15)
        playSur = pygame.Surface(size)

        for i in range(0, 6):
            for j in range(0, 6):
                if enemies[j][i] != 0:
                    enemy((i*70)+ex, (j*35)+ey, i, j)
                    if enemies != [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]:
                        if enemies[5] != [0, 0, 0, 0, 0, 0] and ey+175+35 >= 400:
                            lives = 0
                        elif enemies[4] != [0, 0, 0, 0, 0, 0] and ey+140+35 >= 400:
                            lives = 0
                        elif enemies[3] != [0, 0, 0, 0, 0, 0] and ey+105+35 >= 400:
                            lives = 0
                        elif enemies[2] != [0, 0, 0, 0, 0, 0] and ey+70+35 >= 400:
                            lives = 0
                        elif enemies[1] != [0, 0, 0, 0, 0, 0] and ey+70 >= 400:
                            lives = 0
                        elif enemies[0] != [0, 0, 0, 0, 0, 0] and ey+35 >= 400:
                            lives = 0

        if lives == 3:
            pygame.draw.rect(playSur, (0, 255, 0), prect)
            pygame.draw.rect(playSur, (0, 255, 0), prect2)
        elif lives == 2:
            pygame.draw.rect(playSur, (255, 255, 0), prect)
            pygame.draw.rect(playSur, (255, 255, 0), prect2)
        elif lives == 1:
            pygame.draw.rect(playSur, (230, 0, 0), prect)
            pygame.draw.rect(playSur, (230, 0, 0), prect2)

        if shooting == True and pbxy[0] == 400 and pbxy[1] == 600 and completeTimer == 0 and death == 0:
            pbxy[0] = px+15
            pbxy[1] = 370
            playershot.play()

        if pbxy[1] <= 400 and pbxy[1] >= 0 and lives > 0:
            pbxy[1] -= 10

        if pbxy[1] < 0:
            pbxy[0] = 400
            pbxy[1] = 600

        pygame.draw.rect(playSur, (255, 255, 255), pygame.Rect(pbxy[0]-2, pbxy[1]-5, 4, 10))

        for k in range(len(ebx)-1, -1, -1):
            eby[k] += 10
            pygame.draw.rect(playSur, (255, 255, 255), pygame.Rect(ebx[k]-2, eby[k]-5, 4, 10))
            if ebx[k] >= px and ebx[k] <= px+30 and eby[k] >= 370 and eby[k] <= 400 and lives > 0:
                lives -= 1
                del ebx[k]
                del eby[k]
            elif eby[k] > 400:
                del ebx[k]
                del eby[k]

            elif eby[k] >= 290 and eby[k] <= 339:
                if ebx[k] >= 182 and ebx[k] <= 217:
                    if boulder1[int(floor((eby[k]-290)/7))][int(floor((ebx[k]-182)/7))] == 1:
                        boulder1[int(floor((eby[k]-290)/7))][int(floor((ebx[k]-182)/7))] = 0
                        del ebx[k]
                        del eby[k]
                elif ebx[k] >= 382 and ebx[k] <= 417:
                    if boulder2[int(floor((eby[k]-290)/7))][int(floor((ebx[k]-382)/7))] == 1:
                        boulder2[int(floor((eby[k]-290)/7))][int(floor((ebx[k]-382)/7))] = 0
                        del ebx[k]
                        del eby[k]
                elif ebx[k] >= 582 and ebx[k] <= 617:
                    if boulder3[int(floor((eby[k]-290)/7))][int(floor((ebx[k]-582)/7))] == 1:
                        boulder3[int(floor((eby[k]-290)/7))][int(floor((ebx[k]-582)/7))] = 0
                        del ebx[k]
                        del eby[k]

        for l in range(0, 6):
            for m in range(0, 8):
                boulderPixel(182+(l*7), 290+(m*7), 1, l, m)
                boulderPixel(382+(l*7), 290+(m*7), 2, l, m)
                boulderPixel(582+(l*7), 290+(m*7), 3, l, m)

        for n in range(0, 6):
            if boulder1[7][n] == 0:
                pygame.draw.rect(playSur, (0, 0, 0), pygame.Rect(182+(n*7), 290+(6*7), 7, 7))
            if boulder1[4][n] == 0:
                pygame.draw.rect(playSur, (0, 0, 0), pygame.Rect(182+(n*7), 290+(3*7), 7, 7))
            if boulder2[7][n] == 0:
                pygame.draw.rect(playSur, (0, 0, 0), pygame.Rect(382+(n*7), 290+(6*7), 7, 7))
            if boulder2[4][n] == 0:
                pygame.draw.rect(playSur, (0, 0, 0), pygame.Rect(382+(n*7), 290+(3*7), 7, 7))
            if boulder3[7][n] == 0:
                pygame.draw.rect(playSur, (0, 0, 0), pygame.Rect(582+(n*7), 290+(6*7), 7, 7))
            if boulder3[4][n] == 0:
                pygame.draw.rect(playSur, (0, 0, 0), pygame.Rect(582+(n*7), 290+(3*7), 7, 7))

        if moving == 1 and lives > 0:
            px += 7
        if moving == -1 and lives > 0:
            px -= 7

        if enemies == [[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]] and completeTimer == 0 and lives > 0:
            completeTimer = 90
            score[0] += lives*150

        if death == 0 and lives > 0 and completeTimer == 0:
            updateTicks += 1
            UFOpos -= 5
            if updateTicks == 15 and speed == 2:
                updateTicks = 0
                if estate == 0:
                    estate = 1
                else:
                    estate = 0

                if edirection == "right" and ex < 380:
                    ex += 20
                elif edirection == "right" and ex == 380 and wentDown == False:
                    ey += 20
                    wentDown = True
                elif ex == 380 and wentDown == True:
                    edirection = "left"
                    ex -= 20
                    wentDown = False
                elif edirection == "left" and ex > 20:
                    ex -= 20
                elif edirection == "left" and ex == 20 and wentDown == False:
                    ey += 20
                    wentDown = True
                elif ex == 20 and wentDown == True:
                    edirection = "right"
                    ex += 20
                    wentDown = False

            if estate == 0 and updateTicks == 0:
                shoot()
                enemyshot.play()

        if lives == 0 and death == 0:
            death = 150
            playerexplode.play()

        if death > 0:
            death -= 1
            pygame.draw.circle(playSur, (255, 255, 255), (px, 385), ((300 - death*2) % 30) + 30, 0)

        if death == 1:
            gameState = "over"
            gameover.play()

        if UFOpos <= -28:
            UFOpos = 2400
            UFOshot = False

        if UFOshot == False:
            if pbxy[0] >= UFOpos and pbxy[0] <= UFOpos+28 and pbxy[1] >= 20 and pbxy[1] <= 41:
                UFOshot = True
                score[0] += 500
                pbxy = [400, 600]

            if UFOpos <= 800:
                if UFOpos % 150 < 75:
                    drawUFO1()
                else:
                    drawUFO2()
        
        screen.blit(playSur, (0, 0))

        #This has to be here or the text is drawn over by "playSur"
        if completeTimer > 0:
            completeTimer -= 1
            px = 385
            pbxy = [400, 600]
            ex = 20
            ey = 10
            updateTicks = 1
            ebx = []
            eby = []
            screen.fill((0, 0, 0))
            UFOpos = 2400
            boulder1 = [
            [0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
            ]
            boulder2 = [
            [0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
            ]
            boulder3 = [
            [0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
            ]
            
            if completeTimer > 60:
                screen.blit(ThreeTwoOne3, (360, 125))

            elif completeTimer > 30:
                screen.blit(ThreeTwoOne2, (360, 125))

            else:
                screen.blit(ThreeTwoOne1, (360, 125))

            if completeTimer == 1:
                completeTimer = 0
                enemies = [
                    [1, 1, 1, 1, 1, 1],
                    [2, 2, 2, 2, 2, 2],
                    [3, 3, 3, 3, 3, 3],
                    [4, 4, 4, 4, 4, 4],
                    [5, 5, 5, 5, 5, 5],
                    [6, 6, 6, 6, 6, 6]
                ]

    if gameState == "over":
        screen.fill((0, 0, 0))
        screen.blit(loseText, (170, 150))
        font = pygame.font.SysFont("Sans Serif, Arial, Times New Roman", 50)
        scoreText = font.render("Score: " + str(score[0]), True, (255, 255, 255))
        screen.blit(scoreText, (260, 270))
        gameOverTimer -= 1

        if gameOverTimer == 0:
            gameOverTimer = 200
            gameState = "start"
            lives = 3
            px = 385
            ex = 20
            ey = 10
            enemies = [
                [1, 1, 1, 1, 1, 1],
                [2, 2, 2, 2, 2, 2],
                [3, 3, 3, 3, 3, 3],
                [4, 4, 4, 4, 4, 4],
                [5, 5, 5, 5, 5, 5],
                [6, 6, 6, 6, 6, 6]
            ]
            ebx = []
            eby = []
            death = 0
            completeTimer = 0
            pbxy = [400, 600]
            score[0] = 0
            UFOpos = 2400
            boulder1 = [
            [0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
            ]
            boulder2 = [
            [0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
            ]
            boulder3 = [
            [0, 0, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1]
            ]
    
    pygame.display.flip()
    
    
    
    if px < 0:
        px = 0
    if px > 770:
        px = 770
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit() #sys.exit() is a precaution. Setting "running" to False will, of course, stop loop execution.
        elif event.type == KEYDOWN and event.key == K_LEFT:
            moving = -1
        elif event.type == KEYUP and event.key == K_LEFT:
            moving = 0
        elif event.type == KEYDOWN and event.key == K_RIGHT:
            moving = 1
        elif event.type == KEYUP and event.key == K_RIGHT:
            moving = 0
        elif event.type == KEYDOWN and event.key == K_UP:
            shooting = True
        elif event.type == KEYUP and event.key == K_UP:
            shooting = False
        elif event.type == MOUSEBUTTONDOWN:
            mouseIsPressed = True
        elif event.type == MOUSEBUTTONUP:
            mouseIsPressed = False

