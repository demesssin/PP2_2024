import pygame
import time
import random

# Set up the screen
window_x = 720
window_y = 480
snake_speed = 15

# Colors
black = pygame.Color(0, 0, 0)
white = pygame.Color(255, 255, 255)
red = pygame.Color(255, 0, 0)
green = pygame.Color(0, 255, 0)

# Initialize pygame
pygame.init()
pygame.display.set_caption('Snake Game')
game_window = pygame.display.set_mode((window_x, window_y))

# FPS (frames per second) controller
fps = pygame.time.Clock()

# Snake properties
BLOCK_SIZE = 10

# defining snake default position
snake_position = [100, 50]

# defining first 4 blocks of snake body
snake_body = [[100, 50],
              [90, 50],
              [80, 50],
              [70, 50]
              ]

# fruit position
def generate_food():
    while True:
        fruit_position = [random.randrange(1, (window_x // 10)) * 10,
                          random.randrange(1, (window_y // 10)) * 10]
        if fruit_position not in snake_body:
            return fruit_position

fruit_position = generate_food()

# setting default snake direction towards right
direction = 'RIGHT'
change_to = direction

# initial score and level
score = 0
level = 1

# function to display score
def show_score(font, size):
    score_font = pygame.font.SysFont(font, size)
    score_surface = score_font.render('Score : ' + str(score) + '   Level : ' + str(level), True, white)
    game_window.blit(score_surface, (10, 10))

# function to display game over screen
def game_over():
    my_font = pygame.font.SysFont('times new roman', 50)
    game_over_surface = my_font.render('Your Score is : ' + str(score), True, red)
    game_over_rect = game_over_surface.get_rect()
    game_over_rect.midtop = (window_x / 2, window_y / 4)
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()
    time.sleep(2)
    pygame.quit()
    quit()

# Main Function
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                change_to = 'UP'
            if event.key == pygame.K_DOWN and direction != 'UP':
                change_to = 'DOWN'
            if event.key == pygame.K_LEFT and direction != 'RIGHT':
                change_to = 'LEFT'
            if event.key == pygame.K_RIGHT and direction != 'LEFT':
                change_to = 'RIGHT'

    # If two keys pressed simultaneously, we don't want snake to move into two directions simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    # Moving the snake
    if direction == 'UP':
        snake_position[1] -= BLOCK_SIZE
    if direction == 'DOWN':
        snake_position[1] += BLOCK_SIZE
    if direction == 'LEFT':
        snake_position[0] -= BLOCK_SIZE
    if direction == 'RIGHT':
        snake_position[0] += BLOCK_SIZE

    # Snake body growing mechanism
    snake_body.insert(0, list(snake_position))
    if snake_position[0] == fruit_position[0] and snake_position[1] == fruit_position[1]:
        score += 10
        if score % 30 == 0:  # Increase level after certain score
            level += 1
            snake_speed += 2
        fruit_position = generate_food()
    else:
        snake_body.pop()

    # Border collision check
    if snake_position[0] < 0 or snake_position[0] >= window_x or snake_position[1] < 0 or snake_position[1] >= window_y:
        game_over()

    # Snake self collision check
    if snake_position in snake_body[1:]:
        game_over()

    # Game window background color
    game_window.fill(black)

    # Draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], BLOCK_SIZE, BLOCK_SIZE))

    # Draw fruit
    pygame.draw.rect(game_window, white, pygame.Rect(fruit_position[0], fruit_position[1], BLOCK_SIZE, BLOCK_SIZE))

    # Display score and level
    show_score('times new roman', 20)

    # Refresh game screen
    pygame.display.update()

    # Frame Per Second / Refresh Rate Control
    fps.tick(snake_speed)
