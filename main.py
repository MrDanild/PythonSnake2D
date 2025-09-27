import pygame
import random
import sys

pygame.init()

WIDTH, HEIGHT = 600, 600
GRID_SIZE = 20
FPS = 10



BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 150, 0)
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Змейка")
clock = pygame.time.Clock()


class Segment:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self, surface):
        rect = pygame.Rect(self.x * GRID_SIZE,self.y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface,WHITE,rect)




ingame = True
while ingame:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.time.delay(500)
            pygame.quit()
            sys.exit()
    screen.fill(GREEN)
    pygame.display.update()
