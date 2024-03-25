import pygame

pygame.init()

all_fonts = pygame.font.get_fonts()

for font_name in all_fonts:
    print(font_name)

pygame.quit()