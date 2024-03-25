import pygame

pygame.init()

window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

song_end = pygame.USEREVENT + 1

pygame.mixer.music.set_endevent(song_end)
pygame.mixer.music.load("meow.mp3")
pygame.mixer.music.play()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:  # Исправлено здесь
            if event.key == pygame.K_SPACE:  # И исправлено здесь
                pygame.mixer.music.stop()
                running = False
        if event.type == song_end:
            print("SONG ENDED!")
    window.fill((255, 255, 255))  # Исправлено здесь
    pygame.display.flip()

pygame.quit()
