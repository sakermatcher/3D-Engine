import pygame

size= (1000,1000)
pygame.init()
events = pygame.event.get()

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

surf= pygame.display.set_mode((1000,1000))

screen.fill((0,0,0))