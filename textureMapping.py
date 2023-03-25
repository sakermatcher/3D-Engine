import pygame
import math
from PIL import Image

class texture():
    def __init__(self, imgPath):
        image = Image.open(imgPath)

        # convert the image to RGBA mode
        image_rgba = image.convert('RGBA')

        # get the matrix of RGBA values
        self.img = image_rgba.load()
        
        self.width = image_rgba.size[0]
        self.height = image_rgba.size[1]

        self.lineStop= [] #List with the stop points for y axis
        for i in range(1, self.height+1):
            self.lineStop.append(math.ceil(self.width*i/self.height))

class surface():

    def Reload(self):
        """
        Vertices are in the format [x,y], and they are SW, SE, NE, NW
        """
        SW, SE, NE, NW= self.vertices[0], self.vertices[1], self.vertices[2], self.vertices[3]  #Assign the vertices to their corresponding variables
        xMin = min(SW[0], SE[0], NE[0], NW[0])
        xMax = max(SW[0], SE[0], NE[0], NW[0])
        yMin = min(SW[1], SE[1], NE[1], NW[1])
        yMax = max(SW[1], SE[1], NE[1], NW[1])

        self.width = xMax - xMin
        self.height = yMax - yMin

        self.surface = pygame.Surface((self.width, self.height))

        self.lineForm= [] #List with the line shape
        for i in range()
        self.lineStart= [] #List with the start points for y axis
        for i in range(1, self.height+1):
            self.lineStart.append(math.ceil(self.width*i/self.height))
        
        sumX = texture.height / self.height
        sumY = texture.width / self.width

        drawCounter = 0
        atFromMax= texture.height
        atFromMin= 0

        for i in range(self.height):
            
        
    def __init__(self, vertices, texture):
        self.vertices = vertices
        self.texture = texture
        self.Reload() 




test= texture('img.png')
surface= surface([[0,0], [100,0], [100,100], [0,100]], test)
