import pygame
import random
import math

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((900,500))

# Set title
pygame.display.set_caption("Flappy Bird by Lesiuu")

# Create background
background = pygame.image.load('img_1.png')

# Create bird
birdImg = pygame.image.load('flappy.png')
birdX = 200
birdY = 180
birdY_change = 0.2

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
textX = 10
textY = 10

# Game over font
over_font = pygame.font.Font('freesansbold.ttf', 64)


#Crete rope
ropeImg = []
ropeX = []
ropeX_first = 850
ropeX_change = 500
ropeY = []

for i in range(1000):
    ropeImg.append(pygame.image.load('rope.png'))
    ropeX.append(ropeX_first)
    ropeX_first += ropeX_change
    if i % 2 == 0:
        ropeY.append(random.randint(-200,-100))



    else:
        ropeY.append(random.randint(100,300))



def bird(x,y):
    screen.blit(birdImg, (x, y))



def show_score(x,y):
    score = font.render("Score : " + str(score_value), True, (255,255,255))
    screen.blit(score, (x,y))

def rope(x,y, i):
    screen.blit(ropeImg[i], (x,y))


def collision(birdY,ropeY,i,ropeX):
    if i % 2 == 0:
        if birdY < ropeY+400 and ropeX == 150:
            return True
        else:
            return False
    else:
        if birdY > ropeY and ropeX == 150:
            return True
        else:
            return False

def end_game():
    global ropeX_change
    for i in range(len(ropeImg)):
        ropeX[i] = 100000000
        ropeX_change = 0

    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (450, 200))







# Game loop
running = True

while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                birdY_change = -0.4


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                birdY_change = 0.2




    # Bird movement
    birdY += birdY_change
    if birdY <= 0:
        birdY = 0
    elif birdY >= 480:
        birdY = 480



    bird(150,birdY)

    for i in range(len(ropeImg)):
        ropeX[i] += -0.5
        if ropeX[i] < birdX:
            score_value = i+1
        if collision(birdY,ropeY[i],i,ropeX[i]) == True:
            end_game()
            break
        rope(ropeX[i], ropeY[i],i)

    show_score(textX,textY)
    pygame.display.update()