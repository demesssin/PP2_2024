import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False

font = pygame.font.Font(None, 58)
text = font.render("Aidyn Nigger", True, (0, 100, 54))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)
