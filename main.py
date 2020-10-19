import pygame, sys, random


def ball_movement():
    global ball_speed_x, ball_speed_y, score_b, score_a, score_time
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.top <= 0 or ball.bottom >= height:
        ball_speed_y *= -1
    if ball.left <= 30:
        score_time = pygame.time.get_ticks()
        score_b += 1
    if ball.right >= width - 30:
        score_time = pygame.time.get_ticks()
        score_a += 1
    if ball.colliderect(paddle_a) and ball_speed_x < 0:
        if abs(ball.left - paddle_a.right) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - paddle_a.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - paddle_a.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1
    if ball.colliderect(paddle_b) and ball_speed_x > 0:
        if abs(ball.right - paddle_b.left) < 10:
            ball_speed_x *= -1
        elif abs(ball.bottom - paddle_b.top) < 10 and ball_speed_y > 0:
            ball_speed_y *= -1
        elif abs(ball.top - paddle_b.bottom) < 10 and ball_speed_y < 0:
            ball_speed_y *= -1


def paddle_b_movement():
    paddle_b.y += b_speed
    if paddle_b.bottom >= width:
        paddle_b.bottom = width
    if paddle_b.top <= 0:
        paddle_b.top = 0


# Paddle A's movement is automated
def paddle_a_movement():
    if paddle_a.top < ball.y:
        paddle_a.top += a_speed
    if paddle_a.bottom > ball.y:
        paddle_a.bottom -= a_speed
    if paddle_a.bottom >= width:
        paddle_a.bottom = width
    if paddle_a.top <= 0:
        paddle_a.top = 0


def ball_restart():
    global ball_speed_x, ball_speed_y, score_time

    current_time = pygame.time.get_ticks()
    ball.center = (width // 2, height // 2)
    if current_time - score_time < 700:
        count_three = game_font.render("3", False, WHITE)
        screen.blit(count_three, (width // 2 - 5, height // 2 + 15))
    if 700 < current_time - score_time < 1400:
        count_two = game_font.render("2", False, WHITE)
        screen.blit(count_two, (width // 2 - 5, height // 2 + 15))
    if 1400 < current_time - score_time < 2100:
        count_one = game_font.render("1", False, WHITE)
        screen.blit(count_one, (width // 2 - 5, height // 2 + 15))

    if current_time - score_time < 2100:
        ball_speed_y, ball_speed_x = 0, 0
    else:
        ball_speed_y = 4 * random.choice((1, -1))
        ball_speed_x = 4 * random.choice((1, -1))
        score_time = None


# Global Variable
width = 500
height = 500
WHITE = (255, 255, 255)
dist_from_side = 30
ball_speed_x = 4
ball_speed_y = 4
# Adjust a_speed according to difficulty
a_speed = 4
b_speed = 0
score_a = 0
score_b = 0

pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Pong')
screen.fill((0, 0, 0))
clock = pygame.time.Clock()

# Paddle A
heightA = height // 2
paddle_a = pygame.Rect(dist_from_side, heightA - 25, 10, 50)


# Paddle B
heightB = height // 2
paddle_b = pygame.Rect(width - dist_from_side - 10, heightB - 25, 10, 50)


# Ball
ball_width = 10
init_y = height // 2
init_x = width // 2
ball = pygame.Rect(init_x - (ball_width // 2), init_y - (ball_width // 2), ball_width, ball_width)

# Score Font
game_font = pygame.font.Font('04B_19.ttf.', 20)

# Score Timer
score_time = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                b_speed += 5
            if event.key == pygame.K_UP:
                b_speed -= 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                b_speed -= 5
            if event.key == pygame.K_UP:
                b_speed += 5

    ball_movement()
    paddle_b_movement()
    paddle_a_movement()

    # Visuals
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, WHITE, paddle_a)
    pygame.draw.rect(screen, WHITE, paddle_b)
    pygame.draw.ellipse(screen, WHITE, ball)

    if score_time:
        ball_restart()
    b_score_surface = game_font.render(f"{score_b}", True, WHITE)
    screen.blit(b_score_surface, (265,15))
    a_score_surface = game_font.render(f"{score_a}", True, WHITE)
    screen.blit(a_score_surface, (245, 15))

    pygame.display.flip()
    clock.tick(30)