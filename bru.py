import pygame
import random

pygame.init()

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Гонка")

player_img = pygame.image.load('"C:\Users\abubakr.abrorov\Desktop\Новая папка\photo_2025-04-16_09-29-30.jpg"')  
friend_img = pygame.image.load('"C:\Users\abubakr.abrorov\Desktop\Новая папка\photo_2025-03-07_09-15-51.jpg"')  

player_x = screen_width // 2
player_y = screen_height - 100
player_speed = 5

friend_x = random.randint(0, screen_width - 64)
friend_y = random.randint(0, screen_height - 64)
friend_speed = 3

clock = pygame.time.Clock()

running = True
while running:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed
    
    screen.fill((0, 0, 0))      
    screen.blit(player_img, (player_x, player_y))
    screen.blit(friend_img, (friend_x, friend_y))
    pygame.display.update()
    clock.tick(60)

pygame.quit()

 