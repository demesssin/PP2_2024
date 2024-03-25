import pygame
import random

pygame.init()


def play_next_song():
    global songs
    songs = songs[1:] + [songs[0]]
    pygame.mixer.music.load(songs[0])
    pygame.mixer.music.play()

window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

song_end = pygame.USEREVENT + 1

songs = ['song1.mp3', 'song2.mp3', 'song3.mp3', 'song4.mp3', 'song5.mp3']

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pygame.mixer.music.stop()
                running = False
        if event.type == song_end:
            print("SONG ENDED!")

    play_next_song()
    window.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
