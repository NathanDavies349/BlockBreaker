import pygame
from pygame.locals import *
import GameVariables as GV

#paddle class
class Paddle():
    def __init__(self) -> None:
        self.reset()
    
    def move(self):
        #reset movement direction
        self.direction = 0
        key = pygame.key.get_pressed()#returns the keys that are pressed
        if key[pygame.K_LEFT] and self.rect.left > 0:#if the left arrow key and the left-hand edge of the rectangle is not off of the screen
            self.rect.x -= self.speed
            self.direction = -1
        if key[pygame.K_RIGHT] and self.rect.right < GV.screen_width:#if the left arrow key and the left-hand edge of the rectangle is not off of the screen
            self.rect.x += self.speed
            self.direction = 1

    def draw(self, window):
        pygame.draw.rect(window, self.paddle_colour, self.rect)
        pygame.draw.rect(window, self.paddle_outline, self.rect, 3)#mumber is line thickness
    
    def reset(self) -> None:
        #define paddle variables
        self.height: int = 20
        self.width: int = int(GV.screen_width // 6) #actual code has this as divide by number of columns
        self.x: int = int((GV.screen_width // 2) - (self.width // 2))#centres the paddle
        self.y: int = GV.screen_height - (self.height * 2)#appears twice its own height from the bottom of the screen
        self.speed: int = 10#speed the paddle moves
        self.rect = Rect(self.x, self.y, self.width, self.height)
        self.direction = 0
        #paddle colours
        self.paddle_colour = (142, 135, 123)
        self.paddle_outline = (100, 100, 100)

class Ball():
    def __init__(self, x, y) -> None:
        self.reset(x, y)

    def draw(self, window) -> None:
        pygame.draw.circle(window, self.ball_colour, (self.rect.x + self.ball_radius, self.rect.y + self.ball_radius), self.ball_radius)#when drawing a circle need to define the x and y centre points and a radius
        pygame.draw.circle(window, self.ball_outline, (self.rect.x + self.ball_radius, self.rect.y + self.ball_radius), self.ball_radius, 3)#mumber is line thickness

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




        #check for screen wall collision
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
    
    def reset(self, x, y) -> None:
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
