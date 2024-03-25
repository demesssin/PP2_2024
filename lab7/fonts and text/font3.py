import pygame

def make_font(fonts, size):
    available = pygame.font.get_fonts()
    # get_fonts() возвращает список названий шрифтов без пробелов и в нижнем регистре
    choices = map(lambda x: x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False

font = make_font(['Courier New', 'Times New Roman'], 48)
text = font.render("Hello, World", True, (0, 100, 54))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            done = True

    screen.fill((255, 255, 255))
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
