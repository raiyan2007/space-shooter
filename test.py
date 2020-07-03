import pygame
import os
import time
import random
pygame.font.init()


WIDTH, HEIGHT = 750, 750
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter Tutorial")


# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))

# Background
BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))


class Ship:

    def __init__(self, x, y, health=100):
        self.x = x
        self.y = y
        self.ship_img = RED_SPACE_SHIP


    def draw(self, window):
            window.blit(self.ship_img, (self.x, self.y))



def main():

    run = True
    FPS = 30
    clock = pygame.time.Clock()
    ship = Ship(325,325)

    while run:
        clock.tick(FPS)
        WIN.blit(BG, (0,0))
        ship.draw(WIN)

        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and ship.x > 20:  # left
            ship.x -= 50

        if keys[pygame.K_d] and ship.x < WIDTH - 80:  # right
            ship.x += 50
        if keys[pygame.K_s]:  # down
            ship.y += 50
        if keys[pygame.K_w]:  # up
            ship.y -= 50
main()
