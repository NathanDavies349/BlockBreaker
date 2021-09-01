import GameVariables as GV
import BlocksAndWalls as BW
import Paddle as Pdl


import pygame
from pygame.locals import *


pygame.init()

#initialising the screen
screen = pygame.display.set_mode((GV.screen_width,GV.screen_height))
pygame.display.set_caption('Breakout')
#game variables
game_clock = pygame.time.Clock()#clock object
fps: int = 60#sets the framerate that the clock will run at instead of defaulting to maximum possible




#create wall
wall = BW.Wall()
wall.create_wall()
#create paddle
player_paddle = Pdl.Paddle()


#while loop that runs the game
run = True
while run:
    game_clock.tick(fps)

    screen.fill(GV.background)

    #draw wall
    wall.draw_wall(screen)
    #draw paddle
    player_paddle.draw(screen)
    player_paddle.move()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:#event type that quits the game
            run = False

    pygame.display.update()
pygame.quit()