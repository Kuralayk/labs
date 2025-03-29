import pygame
import sys
import random

pygame.init()

# Game settings
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
SPEED = 5
SCORE = 0
LEVEL = 1

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

font = pygame.font.SysFont("Verdana", 20)

# Generate random food position and weight
# Ensures food does not spawn on the snake

def random_food_position(snake_body):
    while True:
        x = random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE
        y = random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        if (x, y) not in snake_body:
            return x, y

def new_food():
    return {
        "pos": random_food_position(snake),
        "size": random.choice([GRID_SIZE, GRID_SIZE * 1.5, GRID_SIZE * 2]),
        "timer": pygame.time.get_ticks()
    }

snake = [(100, 100), (80, 100), (60, 100)]  # Initial snake position
snake_dir = (GRID_SIZE, 0)  # Initial movement direction
food = new_food()  # First food spawn

clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Handle movement input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and snake_dir != (0, GRID_SIZE):
        snake_dir = (0, -GRID_SIZE)
    if keys[pygame.K_DOWN] and snake_dir != (0, -GRID_SIZE):
        snake_dir = (0, GRID_SIZE)
    if keys[pygame.K_LEFT] and snake_dir != (GRID_SIZE, 0):
        snake_dir = (-GRID_SIZE, 0)
    if keys[pygame.K_RIGHT] and snake_dir != (-GRID_SIZE, 0):
        snake_dir = (GRID_SIZE, 0)
    
    # Move snake
    new_head = (snake[0][0] + snake_dir[0], snake[0][1] + snake_dir[1])
    
    # Check collision with itself or walls
    if new_head in snake or new_head[0] < 0 or new_head[0] >= SCREEN_WIDTH or new_head[1] < 0 or new_head[1] >= SCREEN_HEIGHT:
        running = False
    
    snake.insert(0, new_head)  # Add new head
    
    # Check if food is eaten
    if new_head == food["pos"]:
        SCORE += 1
        if SCORE % 4 == 0:
            LEVEL += 1
            SPEED += 1
        food = new_food()  # Spawn new food
    else:
        snake.pop()  # Remove tail to maintain length
    
    # Check if food should disappear
    if pygame.time.get_ticks() - food["timer"] > 5000:  # 5 seconds
        food = new_food()
    
    # Draw everything
    screen.fill(WHITE)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, GRID_SIZE, GRID_SIZE))
    pygame.draw.rect(screen, RED, (*food["pos"], food["size"], food["size"]))
    
    # Display score and level
    score_text = font.render(f"Score: {SCORE}  Level: {LEVEL}", True, BLACK)
    screen.blit(score_text, (10, 10))
    
    pygame.display.update()
    clock.tick(SPEED)  # Control game speed

pygame.quit()
sys.exit()
