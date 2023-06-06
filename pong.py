import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the paddles and ball
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
BALL_RADIUS = 10

paddle_a = pygame.Rect(50, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle_b = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT/2 - PADDLE_HEIGHT/2, PADDLE_WIDTH, PADDLE_HEIGHT)
ball = pygame.Rect(WIDTH/2 - BALL_RADIUS/2, HEIGHT/2 - BALL_RADIUS/2, BALL_RADIUS, BALL_RADIUS)

# Set up ball movement variables
ball_speed_x = random.choice([-2, 2])
ball_speed_y = random.choice([-2, 2])

# Set up the game clock
clock = pygame.time.Clock()

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the paddles
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle_a.y > 0:
        paddle_a.y -= 3
    if keys[pygame.K_s] and paddle_a.y < HEIGHT - PADDLE_HEIGHT:
        paddle_a.y += 3
    if keys[pygame.K_UP] and paddle_b.y > 0:
        paddle_b.y -= 3
    if keys[pygame.K_DOWN] and paddle_b.y < HEIGHT - PADDLE_HEIGHT:
        paddle_b.y += 3

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Ball collision with paddles
    if ball.colliderect(paddle_a) or ball.colliderect(paddle_b):
        ball_speed_x *= -1

    # Ball collision with walls
    if ball.y > HEIGHT - BALL_RADIUS or ball.y < 0:
        ball_speed_y *= -1

    # Update the window
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, paddle_a)
    pygame.draw.rect(win, WHITE, paddle_b)
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.draw.aaline(win, WHITE, (WIDTH/2, 0), (WIDTH/2, HEIGHT))

    # Refresh the window
    pygame.display.flip()

    # Set the frames per second
    clock.tick(60)

# Quit the game
pygame.quit()
