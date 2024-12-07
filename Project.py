import pygame
import random

# Initialise pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Sprite Collision Game")

# Colours
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Clock to control the frame rate
clock = pygame.time.Clock()
FPS = 60

# Define the player class
class Player(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    def update(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.rect.y -= 5

        if keys[pygame.K_DOWN]:
            self.rect.y += 5

        if keys[pygame.K_LEFT]:
            self.rect.x -= 5

        if keys[pygame.K_RIGHT]:
            self.rect.x += 5

        # Keep player within screen boundaries
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))



# Define the enemy class
class Enemy(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)

# Create sprite groups
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create enemies
for _ in range(7):
    enemy = Enemy()
    all_sprites.add(enemy)
    enemies.add(enemy)

# Score variable
score = 0

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites
    all_sprites.update()

    # Check for collisions
    collided_enemies = pygame.sprite.spritecollide(player, enemies, False)
    if collided_enemies:

        score += len(collided_enemies)
        
        for enemy in collided_enemies:
            # Reset enemy to a new random position
            enemy.rect.x = random.randint(0, SCREEN_WIDTH - enemy.rect.width)
            enemy.rect.y = random.randint(0, SCREEN_HEIGHT - enemy.rect.height)

    # Draw everything
    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Display score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

    # Maintain frame rate
    clock.tick(FPS)

# Quit pygame
pygame.quit()

