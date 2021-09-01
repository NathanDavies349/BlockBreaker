import pygame
import GameVariables as GV

#block class
class Block():
    def set_block_colour(self) -> None:
        #assign colour based on block strength value
        if self.strength == 3:
            self.colour = self.block_blue
        elif self.strength == 2:
            self.colour = self.block_green
        elif self.strength == 1:
            self.colour = self.block_red
    '''
        Apply setters
    '''
    def __init__(self, rectangle_object, strength_value) -> None:
        #defining colours
        self.block_red = (242, 85, 96)
        self.block_green = (86, 174, 87)
        self.block_blue = (69, 177, 232)
        self.rectangle: pygame.Rect() = rectangle_object
        self.strength: int = strength_value
        self.set_block_colour()


#block wall class
class Wall():
    def __init__(self) -> None:
        #define game variables
        self.columns: int = 6
        self.rows: int = 6
        self.width: int = GV.screen_width // self.columns
        self.height: int = 50

    def create_wall(self):    
        self.blocks = []
        for row in range(self.rows):
            #reset block row list
            block_row = []
            #iterate through each column in that row
            for column in range(self.columns):
                #generate x and y co-ordinates for each block and create a rectangle from that
                block_x = column * self.width
                block_y = row * self.height
                #create a pygame rectangle object
                rectangle = pygame.Rect(block_x, block_y, self.width, self.height)
                #assign block strength based on row
                if row < 2:
                    strength: int = 3
                elif row < 4:
                    strength: int = 2
                elif row < 6:
                    strength: int = 1
                #append the individual block to the block row
                block_row.append(Block(rectangle, strength))
            #append row to full list of blocks
            self.blocks.append(block_row)

    def draw_wall(self, window):
        for row in self.blocks:
            for block in row:
                block.set_block_colour()
                pygame.draw.rect(window, block.colour, block.rectangle)
                #add border to each block
                pygame.draw.rect(window, GV.background, block.rectangle, 2)#mumber is line thickness