import pygame
import sys

# ابعاد پنجره
WIDTH, HEIGHT = 800, 600

# رنگ ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# ایجاد پنجره
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# متغیرهای مربوط به مربع
rect = pygame.Rect(350, 500, 100, 100)
speed = 1

# حلقه بازی
while True:
    # پردازش رویدادها
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # حرکت مربع
    keys = pygame.key.get_pressed()
    if rect.x == 0 or rect.x + rect.width == WIDTH:
        speed *= -1
    if rect.y == 0 or rect.y + rect.height == HEIGHT:
        speed *= -1
    if keys[pygame.K_UP]:
        rect.y -= speed
    if keys[pygame.K_DOWN]:
        rect.y += speed
    if keys[pygame.K_LEFT]:
        rect.x -= speed
    if keys[pygame.K_RIGHT]:
        rect.x += speed

    # رسم مربع
    screen.fill(WHITE)
    pygame.draw.rect(screen, BLACK, rect)

    # بروزرسانی صفحه
    pygame.display.flip()
