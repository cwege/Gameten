# Gameten-Simulation
# MBS Digitalwerkstatt
# Dieses Programm steht unter der Lizenz GPLv2

#import random
import pygame, sys
from pygame.locals import *
from random import *
from math import *

pygame.init()
fps = pygame.time.Clock()

#colors
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
BLUE = (0,0,255)


#globals
WIDTH = 400
HEIGHT = 300

#gamet_pos[[x_pos, y_pos, radius, color, delta]]
gamet_pos = [[WIDTH/4, HEIGHT/2, 40, GREEN, 5],
             [WIDTH/2, HEIGHT/4, 10, RED, 30],
             [WIDTH/2, HEIGHT/4, 10, BLUE, 30]
            ]

print ("len: ", len(gamet_pos))

#canvas declaration
window = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)
pygame.display.set_caption('Gameten Simulation')

def update_positions():
    for index in range(len(gamet_pos)):
        delta = gamet_pos[index][4]
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
    

def draw_gamets():
    for gamet in range(len(gamet_pos)):
        pygame.draw.circle(window, gamet_pos[gamet][3],
                           [int( gamet_pos[gamet][0]), int(gamet_pos[gamet][1])], int(gamet_pos[gamet][2]), 0)

def exit_game():
    pygame.quit()
    sys.exit()

    
#main game loop
while True:
    window.fill(BLACK)
    update_positions()

    draw_gamets()    

    for event in pygame.event.get():
        if event.type == QUIT:
            exit_game()
            
    pygame.display.update()
    fps.tick(20)

    for i in range(1,len(gamet_pos)):   
        a = gamet_pos[0][1]-gamet_pos[i][1]
        b = gamet_pos[i][0]-gamet_pos[0][0]
        c=int(sqrt(a*a+b*b))
        print ("distance: 0 to ", i, " : ", c)
        if c < gamet_pos[0][2] + gamet_pos[i][2]:
            exit_game()
