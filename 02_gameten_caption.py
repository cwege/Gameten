# Gameten-Simulation
# MBS Digitalwerkstatt

import pygame

pygame.init()
fps = pygame.time.Clock()

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)

#globals
WIDTH = 800
HEIGHT = 600       

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Gameten Simulation')

#main game loop
while True:

    window.fill(BLACK)

    pygame.display.update()
    fps.tick(60)

