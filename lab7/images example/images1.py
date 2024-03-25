import pygame

# Инициализация Pygame
pygame.init()

# Установка размеров окна
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 400
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

# Создание пустой поверхности
surface = pygame.Surface((100, 100))

# Загрузка изображения
image = pygame.image.load('ball.png')

# Отображение изображения на экране
window.blit(image, (150, 100))  # Примерное местоположение изображения

# Отображение окна
pygame.display.flip()

# Ожидание закрытия окна
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Завершение работы Pygame
pygame.quit()
