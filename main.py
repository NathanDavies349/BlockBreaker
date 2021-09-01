import GameVariables as GV
import BlocksAndWalls as BW
import PaddleAndBall as PB


import pygame
from pygame.locals import *


pygame.init()

#initialising the screen
screen = pygame.display.set_mode((GV.screen_width,GV.screen_height))
pygame.display.set_caption('Breakout')
#game variables
game_clock = pygame.time.Clock()
fps: int = 60#sets the framerate that the clock will run at instead of defaulting to maximum possible

#create wall
wall = BW.Wall()

#create paddle
player_paddle = PB.Paddle()

#create ball
ball = PB.Ball(player_paddle.x + (player_paddle.width//2), player_paddle.y - player_paddle.height)


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

    #draw ball
    ball.draw(screen)
    ball.move(player_paddle, wall)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:#event type that quits the game
            run = False

    pygame.display.update()
pygame.quit()