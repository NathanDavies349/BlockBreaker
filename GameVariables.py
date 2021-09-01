import pygame
pygame.init()
#Setting the dimensions of the screen
screen_width: int = 600
screen_height: int = 600
#Background screen colour
background_colour = (234, 218, 184)
#Text
text_colour = (78, 81, 139)
font = pygame.font.SysFont('Constantia',30)#font and size
#
live_ball = False
game_over = 0