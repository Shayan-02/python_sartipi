import pygame

# تعریف رنگ‌ها
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# تنظیمات صفحه
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("مثلث مساوی‌الأضلاع با طیف رنگی")

# نقاط راس مثلث
points = [(200, 50), (300, 200), (100, 200)]

# رسم مثلث
pygame.draw.polygon(screen, RED, points)

# رسم طیف رنگی
for i in range(len(points)):
    start_color = points[i][0]
    end_color = points[(i + 1) % len(points)][0]
    # for x in range(start_color, end_color + 1):
        # pygame.draw.line(screen, (x, 0, 0), points[i], points[(i + 1) % len(points) - 1])

# آپدیت صفحه و رویدادها
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
