import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import random
import sys

#pygame design
pygame.init()


width = 1925
height = 1025
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

pygame.display.set_caption("Pixel Velocity")

image1= pygame.image.load("images/bg.png")
image2 = pygame.image.load("images/road.png")

image1_1 = pygame.transform.smoothscale(image1, (1925, 1025))
image2_1 = pygame.transform.smoothscale(image2, (1925, 450))
image2_2 = pygame.transform.flip(image2_1, 0, 50)
is_active = True

while is_active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_active = False

    screen.blit(image1_1, (0, 0))
    screen.blit(image2_2, (0, 600))


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()