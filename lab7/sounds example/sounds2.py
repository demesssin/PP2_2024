import pygame

pygame.init()

window_width = 400
window_height = 300
window = pygame.display.set_mode((window_width, window_height))

pygame.mixer.music.load('meow.mp3')

# Воспроизведение звука бесконечно
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False              # что бы закончить цикл мы должны создать пустое окно, а то, дажее нажав пробел цикл на останавоится
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # остановка проигрывания при нажатии на пробел
                pygame.mixer.music.stop()
                running = False
    window.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
