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
        self.max_speed: int = 5
        self.game_over: int = 0
        #ball colours
        self.ball_colour = (142, 135, 123)
        self.ball_outline = (100, 100, 100)

    def draw(self):
        pygame.draw.circle(screen, self.ball_colour, (self.rect.x + self.ball_radius, self.rect.y + self.ball_radius), self.ball_radius)#when drawing a circle need to define the x and y centre points and a radius
        pygame.draw.circle(screen, self.ball_outline, (self.rect.x + self.ball_radius, self.rect.y + self.ball_radius), self.ball_radius, 3)#mumber is line thickness

    def move(self, paddle, wall) -> int:
        collision_threshold: int = 5

        #start off with assumption that the wall is completely destroyed
        wall_destroyed = True
        for row_count, row in enumerate(wall.blocks):
            for item_count, block in enumerate(row):
                #check collision
                if self.rect.colliderect(block.rectangle):
                    #check if collision was from above
                    if abs(self.rect.bottom - block.rectangle.top) < collision_threshold  and self.speed_y > 0:
                        self.speed_y *= -1
                    #check if collision was from below
                    if abs(self.rect.top - block.rectangle.bottom) < collision_threshold  and self.speed_y < 0:
                        self.speed_y *= -1
                    #check if collision was from left
                    if abs(self.rect.right - block.rectangle.left) < collision_threshold  and self.speed_x > 0:
                        self.speed_x *= -1
                    #check if collision was from right
                    if abs(self.rect.left - block.rectangle.right) < collision_threshold  and self.speed_x < 0:
                        self.speed_x *= -1

                    #reduce block strength
                    if block.strength > 1:
                        block.strength -= 1
                    else:
                        block.rectangle = (0,0,0,0)#reset the rectangle properties
                #check if block still exists, then wall is not destroyed
                if block.rectangle != (0,0,0,0):
                    wall_destroyed = False
        #check if wall is destroyed
        if wall_destroyed == True:
            self.game_over = 1 #won the game




        #check for wall collision
        if self.rect.left < 0 or self.rect.right > GV.screen_width:
            self.speed_x *= -1
        #check for top and bottom collision
        if self.rect.top < 0:
            self.speed_y *= -1
        if self.rect.bottom > GV.screen_height:
            self.game_over = -1
        
        #look for paddle collision
        if self.rect.colliderect(paddle):
            #top collision
            if abs(self.rect.bottom - paddle.rect.top) < collision_threshold and self.speed_y > 0:#ball must be travelling downwards, could get stuck in a collisional loop if this is not implemented
                self.speed_y *= -1
                self.speed_x += paddle.direction
                if self.speed_x > self.max_speed:
                    self.speed_x = self.max_speed
                elif self.speed_x < 0 and self.speed_x < -self.max_speed:#is the <0 condition necessary
                    self.speed_x = -self.max_speed
            else:#collision with side of the paddle
                self.speed_x *= -1


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
    ball.move(player_paddle, wall)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:#event type that quits the game
            run = False

    pygame.display.update()
pygame.quit()