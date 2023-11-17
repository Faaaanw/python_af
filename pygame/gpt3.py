import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BACKGROUND_COLOR = (0, 0, 0)
PADDLE_COLOR = (0, 255, 0)
BALL_COLOR = (255, 255, 255)
BRICK_COLOR = (255, 0, 0)
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
BALL_SIZE = 20
BRICK_WIDTH = 80
BRICK_HEIGHT = 20
BALL_SPEED = 5

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Brick Breaker")

# Initialize the paddle
paddle = pygame.Rect(WIDTH // 2 - PADDLE_WIDTH // 2, HEIGHT - 2 * PADDLE_HEIGHT, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_speed = 0

# Initialize the ball
ball = pygame.Rect(WIDTH // 2 - BALL_SIZE // 2, HEIGHT // 2 - BALL_SIZE // 2, BALL_SIZE, BALL_SIZE)
ball_direction = [random.choice((1, -1)), -1]

# Initialize the bricks
bricks = []
for row in range(5):
    for col in range(10):
        brick = pygame.Rect(col * (BRICK_WIDTH + 5) + 30, row * (BRICK_HEIGHT + 5) + 50, BRICK_WIDTH, BRICK_HEIGHT)
        bricks.append(brick)

# Game variables
font = pygame.font.Font(None, 36)
score = 0

# Function to move the paddle
def move_paddle():
    paddle.x += paddle_speed
    if paddle.x < 0:
        paddle.x = 0
    elif paddle.x > WIDTH - PADDLE_WIDTH:
        paddle.x = WIDTH - PADDLE_WIDTH

# Function to move the ball
def move_ball():
    ball.x += ball_direction[0] * BALL_SPEED
    ball.y += ball_direction[1] * BALL_SPEED

# Function to handle collisions with walls and paddle
def handle_collisions():
    if ball.x < 0 or ball.x > WIDTH - BALL_SIZE:
        ball_direction[0] *= -1
    if ball.y < 0:
        ball_direction[1] = 1
    if ball.colliderect(paddle):
        ball_direction[1] = -1

# Function to handle collisions with bricks
def handle_brick_collisions():
    global score
    for brick in bricks[:]:
        if ball.colliderect(brick):
            ball_direction[1] *= -1
            bricks.remove(brick)
            score += 10

# Function to draw objects on the screen
def draw_objects():
    screen.fill(BACKGROUND_COLOR)
    pygame.draw.rect(screen, PADDLE_COLOR, paddle)
    pygame.draw.rect(screen, BALL_COLOR, ball)

    for brick in bricks:
        pygame.draw.rect(screen, BRICK_COLOR, brick)

    score_text = font.render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                paddle_speed = -5
            if event.key == pygame.K_RIGHT:
                paddle_speed = 5

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                paddle_speed = 0

    move_paddle()
    move_ball()
    handle_collisions()
    handle_brick_collisions()

    draw_objects()

    pygame.display.flip()
    clock.tick(60)

# Game over screen
game_over_text = font.render(f"Game Over - Your Score: {score}", True, (255, 255, 255))
screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 20))
pygame.display.flip()

# Wait for a few seconds before closing the game
pygame.time.delay(3000)

pygame.quit()
sys.exit()
