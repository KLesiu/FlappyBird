import pygame

# Initialize pygame
pygame.init()

# Create the screen
screen = pygame.display.set_mode((900,504))

# Create background
background = pygame.image.load('img_1.png')

# Create bird
birdImg = pygame.image.load('flappy.png')
birdX = 150
birdY = 180


# Game loop
running = True

while running:
    screen.fill((0,0,0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(birdImg, (birdX,birdY))
    pygame.display.update()