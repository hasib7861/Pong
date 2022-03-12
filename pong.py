# Pong by Hasib

import pygame

WIDTH = 800
HEIGHT = 600
FPS = 30

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


class Paddle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((30, 80))
        self.image.fill(WHITE)
        self.x = x
        self.y = y
        self.rect = pygame.Rect((self.x, self.y), (30, 80))
        self.rect.centerx = self.x
        self.rect.centery = HEIGHT / 2
        self.speed = 1

    def update(self):
        pass


all_sprites = pygame.sprite.Group()
pA = Paddle(40, HEIGHT/2)
pB = Paddle(760, HEIGHT/2)
all_sprites.add(pA)
all_sprites.add(pB)
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

    # Draw / render
    screen.fill(BLACK)
    all_sprites.draw(screen)
    # *after* drawing everything, flip the display
    pygame.display.flip()