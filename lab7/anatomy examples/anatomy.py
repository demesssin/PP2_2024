import pygame

pygame.init()
screen = pygame.display.set_mode((400, 300))
done = False
is_blue = True
x = 80
y = 80

clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get():
        pygame.draw.rect(screen, (0, 128, 255), pygame.Rect(30, 30, 100, 100))
        if event.type == pygame.QUIT:
            done = True

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            is_blue = not is_blue

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_UP]:
        y = y - 3
    if pressed[pygame.K_DOWN]:
        y = y + 3
    if pressed[pygame.K_LEFT]:
        x = x - 3
    if pressed[pygame.K_RIGHT]:
        x = x + 3

    screen.fill((0, 0, 0))
    if is_blue:
        color = (0, 128, 255)
    else:
        color = (255, 100, 0)
    pygame.draw.rect(screen, color, pygame.Rect(x, y, 100, 100))
    pygame.display.flip()
    clock.tick(60)
