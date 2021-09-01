import pygame
from pygame.locals import *
import GameVariables as GV

#paddle class
class Paddle():
    def __init__(self) -> None:
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