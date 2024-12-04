import pygame
from os.path import join

WINDOW_WIDTH, WINDOW_HEIGHT = 1280, 720

# general setup
pygame.init()

display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

pygame.display.set_caption('Space Shooter')

# image
player_sprite_path = join('images', 'player.png')
player_sprite = pygame.image.load(player_sprite_path).convert_alpha()

running = True

while running:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # draw teh game

    display.fill('RED')
    
    display.blit(player_sprite, (x,50))
    x += 0.1
    if x > WINDOW_WIDTH:
        x = 0
    
    pygame.display.update()

pygame.quit()