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
game_clock = pygame.time.Clock()
fps: int = 60#sets the framerate that the clock will run at instead of defaulting to maximum possible

class Ball():
    def __init__(self, x, y) -> None:
        #ball variables
        self.ball_radius: int = 10
        self.x = x - self.ball_radius #centralises the ball
        self.y = y
        self.rect = Rect(self.x, self.y, self.ball_radius*2, self.ball_radius*2)
        self.speed_x: int = 4
        self.speed_y: int = -4#negative is going up the screen
        self.game_over: int = 0
        #ball colours
        self.ball_colour = (142, 135, 123)
        self.ball_outline = (100, 100, 100)

    def draw(self):
        pygame.draw.circle(screen, self.ball_colour, (self.rect.x + self.ball_radius, self.rect.y + self.ball_radius), self.ball_radius)#when drawing a circle need to define the x and y centre points and a radius
        pygame.draw.circle(screen, self.ball_outline, (self.rect.x + self.ball_radius, self.rect.y + self.ball_radius), self.ball_radius, 3)#mumber is line thickness

    def move(self) -> int:

        #check for wall collision
        if self.rect.left < 0 or self.rect.right > GV.screen_width:
            self.speed_x *= -1
        #check for top and bottom collision
        if self.rect.top < 0:
            self.speed_y *= -1
        elif self.rect.bottom > GV.screen_height:
            self.game_over = -1

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        return self.game_over

#create wall
wall = BW.Wall()
wall.create_wall()
#create paddle
player_paddle = Pdl.Paddle()
#create ball
ball = Ball(player_paddle.x + (player_paddle.width//2), player_paddle.y - player_paddle.height)


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
    ball.draw()
    ball.move()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:#event type that quits the game
            run = False

    pygame.display.update()
pygame.quit()