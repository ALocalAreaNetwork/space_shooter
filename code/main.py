import pygame

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# general setup
pygame.init()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Space Shooter')

running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw teh game

    display.fill('RED')

    pygame.display.update()

pygame.quit()