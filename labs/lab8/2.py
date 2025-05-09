import pygame
import sys
import random

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
SPEED = 5
SCORE = 0
LEVEL = 1

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Verdana", 20)

def random_food_position(snake_body):
    while True:
        x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (x, y) not in snake_body:
            return x, y

snake = [(100, 100), (80, 100), (60, 100)]
snake_dir = (GRID_SIZE, 0)
food = random_food_position(snake)

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, GRID_SIZE):
        snake_dir = (0, -GRID_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -GRID_SIZE):
        snake_dir = (0, GRID_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (GRID_SIZE, 0):
        snake_dir = (-GRID_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-GRID_SIZE, 0):
        snake_dir = (GRID_SIZE, 0)
    
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    if new_head in snake or new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
        running = False
    
    snake.insert(0, new_head)
    
    if new_head == food:
        SCORE += 1
        if SCORE % 4 == 0:
            LEVEL += 1
            SPEED += 1
        food = random_food_position(snake)
    else:
        snake.pop()
    

    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (*food, GRID_SIZE, GRID_SIZE))
    
    
    score_text = font.render(f"Score: {SCORE}  Level: {LEVEL}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(SPEED)

pygame.quit()
sys.exit()

