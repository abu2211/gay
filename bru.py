import pygame
import random

# Инициализация Pygame
pygame.init()

# Размеры окна
screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Гонка")

# Загрузка изображений
player_img = pygame.image.load('"C:\Users\abubakr.abrorov\Desktop\Новая папка\photo_2025-04-16_09-29-30.jpg"')  # Замените на путь к своему изображению
friend_img = pygame.image.load('"C:\Users\abubakr.abrorov\Desktop\Новая папка\photo_2025-03-07_09-15-51.jpg"')  # Замените на путь к фото друга

# Начальная позиция игрока
player_x = screen_width // 2
player_y = screen_height - 100
player_speed = 5

# Начальная позиция друга (он будет случайно двигаться)
friend_x = random.randint(0, screen_width - 64)
friend_y = random.randint(0, screen_height - 64)
friend_speed = 3

# FPS
clock = pygame.time.Clock()

# Главный цикл игры
running = True
while running:
    # Проверка событий (например, нажатие клавиш)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Обработка нажатий клавиш для движения
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Очистка экрана
    screen.fill((0, 0, 0))  # Чёрный фон

    # Рисуем игрока (картинку)
    screen.blit(player_img, (player_x, player_y))

    # Рисуем друга (картинку)
    screen.blit(friend_img, (friend_x, friend_y))

    # Обновляем экран
    pygame.display.update()

    # Устанавливаем FPS
    clock.tick(60)

pygame.quit()

 