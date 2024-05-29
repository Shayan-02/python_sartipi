import pygame
import sys

# ابعاد پنجره
WIDTH, HEIGHT = 800, 600

# رنگ ها
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# ایجاد پنجره
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# مختصات مثلث
x1, y1 = WIDTH // 2 - 100, HEIGHT // 2
x2, y2 = WIDTH // 2, HEIGHT // 2 + 150
x3, y3 = WIDTH // 2 + 100, HEIGHT // 2

# حلقه بازی
while True:
    # پردازش رویدادها
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # رسم مثلث
    screen.fill((255, 255, 255))  # پس زمینه سفید
    pygame.draw.polygon(screen, RED, ((x1, y1), (x2, y2), (x3, y3)))
    pygame.draw.polygon(screen, GREEN, ((x1, y1), (x2, y2), (x3, y3)), 5)
    pygame.draw.polygon(screen, BLUE, ((x1, y1), (x2, y2), (x3, y3)), 10)
    pygame.draw.polygon(screen, YELLOW, ((x1, y1), (x2, y2), (x3, y3)), 15)

    # ترکیب رنگ های زاویه مثلث
    pygame.draw.polygon(screen, (255, 128, 0), ((x1, y1), (x2, y2), (x3, y3)), 20)

    # بروزرسانی صفحه
    pygame.display.flip()
