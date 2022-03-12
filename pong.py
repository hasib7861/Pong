# Pong by Hasib

import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30
score_A = 0
score_B = 0

# Define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 255, 0)
GREEN = (0, 0, 255)

# Initialize pygame and create window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")
clock = pygame.time.Clock()
font_name = pygame.font.match_font('arial')


def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y, paddle_num):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 80))
        self.image.fill(WHITE)
        self.paddle_num = paddle_num
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.speedy = 0

    def update(self):
        self.speedy = 0

        if self.paddle_num == 1:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_w]:
                self.speedy -= 20
            if keystate[pygame.K_s]:
                self.speedy += 20
            self.rect.y += self.speedy

        if self.paddle_num == 2:
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_UP]:
                self.speedy -= 20
            if keystate[pygame.K_DOWN]:
                self.speedy += 20
            self.rect.y += self.speedy

        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= 520:
            self.rect.y = 520



class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = 590
        self.speedx = 5
        self.speedy = 5
        self.score_A = 0
        self.score_B = 0

    def update(self):
        self.score_A = 0
        self.score_B = 0
        self.rect.x += self.speedx
        self.rect.y += self.speedy

        if self.rect.x <= 0:
            self.score_B += 1
            self.rect.x = 0
            self.speedx *= -1
        elif self.rect.x >= 780:
            self.score_A += 1
            self.rect.x = 780
            self.speedx *= -1
        elif self.rect.y <= 0:
            self.rect.y = 0
            self.speedy *= -1
        elif self.rect.y >= 580:
            self.rect.y = 580
            self.speedy *= -1

        # Paddle-Ball Collisions
        # TODO: Refine collisions so it looks less buggy
        for paddle in paddles:
            if (paddle.rect.x + 30 >= self.rect.x >= paddle.rect.x - 20) and (paddle.rect.y + 50 >= self.rect.y >= paddle.rect.y - 50):
                self.speedx *= -1


all_sprites = pygame.sprite.Group()
paddles = pygame.sprite.Group()
pA = Paddle(40, HEIGHT / 2, 1)
pB = Paddle(760, HEIGHT / 2, 2)
ball = Ball(WIDTH / 2, HEIGHT / 2)
all_sprites.add(pA, pB, ball)
paddles.add(pA, pB)
# Game loop
running = True
while running:
    clock.tick(FPS)

    # Process inputs (events)
    for event in pygame.event.get():
        # Check for closing the window
        if event.type == pygame.QUIT:
            running = False

    # Update
    all_sprites.update()
    score_A += ball.score_A
    score_B += ball.score_B

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    draw_text(screen, f"Score A: {str(score_A)}   Score B: {str(score_B)}", 25, WIDTH / 2, 10)
    # *after* drawing everything, flip the display
    pygame.display.flip()