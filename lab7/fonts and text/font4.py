import pygame

_cached_fonts = {}

def make_font(fonts, size):
    available = pygame.font.get_fonts()
    choices = map(lambda x: x.lower().replace(' ', ''), fonts)
    for choice in choices:
        if choice in available:
            return pygame.font.SysFont(choice, size)
    return pygame.font.Font(None, size)

def get_font(font_preferences, size):
    global _cached_fonts
    key = str(font_preferences) + '|' + str(size)
    font = _cached_fonts.get(key, None)
    if font is None:
        font = make_font(font_preferences, size)
        _cached_fonts[key] = font
    return font

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
done = False

font = get_font(['Arial', 'Courier New', 'Times New Roman'], 48)
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
