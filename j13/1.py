import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
RECT_WIDTH, RECT_HEIGHT = 100, 50
SOUND_FILE = "click.mp3"  # replace with your own sound file

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the rectangle
rect = pygame.Rect(
    WIDTH / 2 - RECT_WIDTH / 2, HEIGHT / 2 - RECT_HEIGHT / 2, RECT_WIDTH, RECT_HEIGHT
)

# Load the sound file
sound = pygame.mixer.Sound(SOUND_FILE)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                sound.play()

    # Draw the rectangle
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0, 0, 255), rect)
    pygame.display.flip()
