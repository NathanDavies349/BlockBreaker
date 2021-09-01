import GameVariables as GV
import BlocksAndWalls as BW
import PaddleAndBall as PB

import pygame
from pygame.locals import *

#function to output text to screen
def draw_text(text, font, text_colour, x, y, window):
    img = font.render(text, True, text_colour)
    window.blit(img, (x,y))#blit function places image onto screen



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

    screen.fill(GV.background_colour)

    #draw all objects
    wall.draw_wall(screen)
    player_paddle.draw(screen)
    ball.draw(screen)

    #game controls active if ball still in play
    if GV.live_ball:
        player_paddle.move()
        GV.game_over = ball.move(player_paddle, wall)
        if GV.game_over != 0:
            GV.live_ball = False
    
    #print player instructions
    if not GV.live_ball:
        if GV.game_over == 0:#game not started
            draw_text('CLICK ANYWHERE TO START', GV.font, GV.text_colour, 100, GV.screen_height//2 + 100, screen)
        elif GV.game_over == 1:#game won
            draw_text('YOU WON', GV.font, GV.text_colour, 240, GV.screen_height//2 + 50, screen)
            draw_text('CLICK ANYWHERE TO START', GV.font, GV.text_colour, 100, GV.screen_height//2 + 100, screen)
        elif GV.game_over == -1:#game lost
            draw_text('GAME OVER', GV.font, GV.text_colour, 200, GV.screen_height//2 + 50, screen)
            draw_text('CLICK ANYWHERE TO START', GV.font, GV.text_colour, 100, GV.screen_height//2 + 100, screen)
    


    for event in pygame.event.get():
        if event.type == pygame.QUIT:#event type that quits the game
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN and GV.live_ball == False:#Game starts on click
            GV.live_ball = True
            ball.reset(player_paddle.x + (player_paddle.width//2), player_paddle.y - player_paddle.height)
            player_paddle.reset()
            wall.create_wall()


    pygame.display.update()
pygame.quit()