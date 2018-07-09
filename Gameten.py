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
WIDTH = 200
HEIGHT = 150

gamet_pos = [[WIDTH/4, HEIGHT/2],[WIDTH/2, HEIGHT/4]]

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Gameten Simulation')

def update_position(index, delta):
    gamet_pos[index][0] = gamet_pos[index][0] + randint(-delta, delta)
    gamet_pos[index][1] = gamet_pos[index][1] + randint(-delta, delta)
    if gamet_pos[index][0] < 0:
        gamet_pos[index][0] = -gamet_pos[index][0]
    if gamet_pos[index][0] > WIDTH:
        gamet_pos[index][0] = 2*WIDTH-gamet_pos[index][0]
    if gamet_pos[index][1] < 0:
        gamet_pos[index][1] = -gamet_pos[index][1]
    if gamet_pos[index][1] > HEIGHT:
        gamet_pos[index][1] = 2*HEIGHT-gamet_pos[index][1]
    

def draw_gamet(color, gamet, size):
    pygame.draw.circle(window, color,
                       [int( gamet_pos[gamet][0]), int(gamet_pos[gamet][1])], size, 0)

#main game loop
while True:
    
    window.fill(BLACK)

    update_position(0, 5)
    update_position(1, 30)

    draw_gamet(GREEN, 0, 20)    
    draw_gamet(RED, 1, 10)    

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(20)

