import pygame
import random

# Initialize the game engine
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))

# Load the player and enemy images
player_image = pygame.image.load("player.png").convert_alpha()
enemy_image = pygame.image.load("enemy.png").convert_alpha()

# Set up the player and enemy rectangles
player_rect = player_image.get_rect()
enemy_rect = enemy_image.get_rect()

# Initialize the player and enemy positions
player_rect.x = 400
player_rect.y = 500
enemy_rect.x = random.randint(0, 750)
enemy_rect.y = random.randint(50, 100)

# Initialize the player's bullet list
bullets = []

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Handle the player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_rect.x -= 5
            if event.key == pygame.K_RIGHT:
                player_rect.x += 5
            if event.key == pygame.K_UP:
                player_rect.y -= 5
            if event.key == pygame.K_DOWN:
                player_rect.y += 5
            if event.key == pygame.K_SPACE:
                bullet_rect = pygame.Rect(player_rect.x + 20, player_rect.y, 10, 10)
                bullets.append(bullet_rect)

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the player and enemy
    screen.blit(player_image, player_rect)
    screen.blit(enemy_image, enemy_rect)

    # Move the player's bullets
    for bullet in bullets:
        bullet.y -= 5
        pygame.draw.rect(screen, (0, 0, 0), bullet)

    # Check if the player's bullet has hit the enemy
    for bullet in bullets:
        if bullet.colliderect(enemy_rect):
            enemy_rect.x = random.randint(0, 750)
            enemy_rect.y = random.randint(50, 100)

    # Update the display
    pygame.display.flip()

# Quit the game
pygame.quit()
