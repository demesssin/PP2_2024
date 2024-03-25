import pygame

pygame.init()

# Загрузка звука
pygame.mixer.music.load('meow.mp3')

# Воспроизведение звука
pygame.mixer.music.play(0)

# Ожидание завершения проигрывания
while pygame.mixer.music.get_busy():
    continue

# Завершение работы Pygame
pygame.quit()
