# Gameten-Simulation
# MBS Digitalwerkstatt
# Dieses Programm steht unter der Lizenz GPLv2

#import random
import pygame, sys
from pygame.locals import *
from random import *

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

gamet_pos = [WIDTH/2, HEIGHT/2]

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Gameten Simulation')

#main game loop
while True:
    
    window.fill(BLACK)

    gamet_pos[0] = gamet_pos[0] + randint(-5, 5)
    gamet_pos[1] = gamet_pos[1] + randint(-5, 5)

    pygame.draw.circle(window, WHITE,
                       [int(gamet_pos[0]), int(gamet_pos[1])], 20, 0)

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(20)

