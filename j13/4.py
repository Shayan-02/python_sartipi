import pygame

# Initialize Pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the rectangle
rect = pygame.Rect(WIDTH / 2 - 50, HEIGHT / 2 - 50, 100, 100)

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Fill the screen with white
    screen.fill((255, 255, 255))

    # Get the current mouse position
    mouse_pos = pygame.mouse.get_pos()

    # Change the color of the rectangle based on the x-coordinate of the mouse
    if mouse_pos[0] < WIDTH / 2:
        rect_color = (255, 0, 0)  # red
    else:
        rect_color = (0, 0, 255)  # blue

    pygame.draw.rect(screen, rect_color, rect)

    # Update the display
    pygame.display.flip()