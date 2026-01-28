import pygame
from command_router import route_command

pygame.init()

WIDTH, HEIGHT = 800, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Robot Control")

WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.SysFont(None, 40)

buttons = {
    "forward": pygame.Rect(350, 50, 100, 80),
    "left": pygame.Rect(200, 150, 100, 80),
    "stop": pygame.Rect(350, 150, 100, 80),
    "right": pygame.Rect(500, 150, 100, 80),
    "back": pygame.Rect(350, 250, 100, 80),
}

def draw():
    screen.fill(WHITE)
    for text, rect in buttons.items():
        color = RED if text == "stop" else GRAY
        pygame.draw.rect(screen, color, rect)
        label = font.render(text.upper(), True, BLACK)
        screen.blit(label, (rect.x + 10, rect.y + 25))
    pygame.display.update()

running = True
while running:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            for cmd, rect in buttons.items():
                if rect.collidepoint(event.pos):
                    route_command("screen", cmd)

pygame.quit()
