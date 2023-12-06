import sys
import pygame

class Material(object):
    def __init__(self, name, pos, radius, gravity):
        self.name = name
        self.x = pos[0]
        self.y = pos[1]
        self.radius = radius
        self.gravity = gravity

allsands = []

def game():
    pygame.init()
    win = pygame.display.set_mode((1000, 650))
    pygame.display.set_caption("Sand")
    clock = pygame.time.Clock()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                print(event.pos)
                allsands.append(Material("Sand", event.pos, 5, 2))

        win.fill((0,0,0,))
        for sand in allsands:
            pygame.draw.circle(win, (194, 178, 128), (sand.x, sand.y), sand.radius)
            if sand.y >=0 and sand.y < 645:
                sand.y += sand.gravity

        pygame.display.update()
        clock.tick(50)

game()
