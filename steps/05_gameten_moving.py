# Gameten-Simulation
# MBS Digitalwerkstatt

#import random
import pygame, sys
from pygame.locals import *

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
GAMET_RADIUS = 20
gamet_pos = [0,0]

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Gameten Simulation')

gamet_pos = [WIDTH/4, HEIGHT/4]

#update positions
def update_pos():
    global gamet_pos

    #update gamet pos
    gamet_pos[0] += 0.5
    gamet_pos[1] += 0.5

        
#draw function of canvas
def draw(canvas):
    global gamet_pos, gamet_vel
           
    canvas.fill(BLACK)

    #draw gamet
    pygame.draw.circle(canvas, RED,
                       [int(gamet_pos[0]), int(gamet_pos[1])], 20, 0)


#main game loop
while True:

    update_pos()
    draw(window)

    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fps.tick(60)

