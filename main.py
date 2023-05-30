import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((900,504))

# Create background
background = pygame.image.load('img_1.png')

# Create bird
birdImg = pygame.image.load('flappy.png')

birdY = 180
birdY_change = 0.2


def bird(x,y):
    screen.blit(birdImg, (x, y))


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
    bird(150,birdY)

    pygame.display.update()