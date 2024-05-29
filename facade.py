import pygame, sys, random
from pygame.locals import *
pygame.init()
 
# Colours
BACKGROUND = (255, 255, 255)
HEXAGON = (50, 200, 50)
BOX = (50, 50, 200)
 
# Game Setup
FPS = 60
fpsClock = pygame.time.Clock()
WINDOW_WIDTH = 400
WINDOW_HEIGHT = 300
 
WINDOW = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('My Game!')

class HexButton : 
    def __init__ (self, coordinates) :
        self.Xcoordinate = coordinates[0]
        self.Ycoordinate = coordinates[1]
        self.squareColour = BOX
        self.hexagonColour = HEXAGON
        self.hexagon = Hexagon(self.Xcoordinate, self.Ycoordinate + 5, self.hexagonColour)
        self.square = Square(self.Xcoordinate + 85, self.Ycoordinate, self.squareColour)
        
    
    def render (self) : 
        self.square.render()
        self.hexagon.render()

    def set_coordinates(self, coordinates):
        self.Xcoordinate = coordinates[0]
        self.Ycoordinate = coordinates[1]

        self.hexagon.set_coordinates(coordinates[0], coordinates[1])
        self.square.set_coordinates(coordinates[0], coordinates[1])
        

class Shape :
    def __init__ (self, Xcoordinate, Ycoordinate, colour) :
        self.colour = colour
        self.Xcoordinate = Xcoordinate
        self.Ycoordinate = Ycoordinate
    
    def set_coordinates(self, Xcoordinate, Ycoordinate):
        self.Xcoordinate = Xcoordinate
        self.Ycoordinate = Ycoordinate
        

class Hexagon (Shape) :
    def render (self) :
        point1 = [self.Xcoordinate, self.Ycoordinate + 25]
        point2 = [self.Xcoordinate + 25, self.Ycoordinate]
        point3 = [self.Xcoordinate + 100, self.Ycoordinate]
        point4 = [self.Xcoordinate + 125, self.Ycoordinate + 25]
        point5 = [self.Xcoordinate + 100, self.Ycoordinate + 50]
        point6 = [self.Xcoordinate + 25, self.Ycoordinate + 50]
        hexagon_coords = [point1, point2, point3, point4, point5, point6]
        #hexagon_coords = [[50,50], [75,25], [150, 25], [175, 50], [150, 75], [75, 75]]
        pygame.draw.polygon(WINDOW, self.colour, hexagon_coords)
    
    
class Square (Shape): 
    def render (self) :
        rectangle1 = pygame.Rect(self.Xcoordinate, self.Ycoordinate, 60, 60)
        pygame.draw.rect(WINDOW, self.colour, rectangle1)

    
 
# The main function that controls the game
def main () :
    button = HexButton([90, 90])


    
    looping = True

    # The main game loop
    while looping :
        # Get inputs
        for event in pygame.event.get() :
            if event.type == QUIT :
                pygame.quit()
                sys.exit()

        # Processing
        # This section will be built out later
        #rectangle1 = pygame.Rect(135, 20, 60, 60)
        #hexagon_coords = [[50,50], [75,25], [150, 25], [175, 50], [150,75], [75, 75]]


        #w = random.randrange(0, WINDOW_WIDTH)
        #h = random.randrange(0, WINDOW_HEIGHT)
        #print(w)
        #button.set_coordinates([w, h])
        # Render elements of the game
        WINDOW.fill(BACKGROUND)
        button.render()
        #pygame.draw.rect(WINDOW, BOX, rectangle1)
        #pygame.draw.polygon(WINDOW, HEXAGON, hexagon_coords)
        pygame.display.update()
        fpsClock.tick(FPS)
 
main()