import pygame
import PySimpleGUI as sg
from forms import cube, pyramid
from engine import py
from math import cos, sin, acos
from math import degrees as deg
from math import radians as rad
import time

size= (800,800)
pygame.init()
events = pygame.event.get()
forms=[cube, pyramid]
form=False

dims= [5,5,5] #cube dims xyz\n
pc= [5,5,5] #perspective coordinates\n
pa= [5,5,5] #perspective angles\n
start= [0,0,0]

layout= [
    [sg.Text('dims (xyz):'), sg.Input('5', k='x', size=(3,1)), sg.Input('5',k='y', size=(3,1)), sg.Input('5',k='z', size=(3,1))],
    [sg.Text('UrAt (x,y,z):'), sg.Input('5',k='ux', size=(3,1)), sg.Input('5',k='uy', size=(3,1)), sg.Input('5',k='uz', size=(3,1))],
    [sg.Text('view (d,ax,ay):'), sg.Input('5',k='d', size=(3,1)), sg.Input('5',k='ax', size=(3,1)), sg.Input('5',k='ay', size=(3,1))],
    [sg.Button('submit', k='s'), sg.Button('change form', k='f'), sg.Button('rotate', k='r')]

]

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

surf= pygame.display.set_mode((800,800))
window= sg.Window('cube', layout)

def render():
    screen.fill((0,0,0))
    p= forms[int(form)](dims, pc, pa, start)
    for v1 in p[1].keys():
        for v2 in p[1][v1]:
            pygame.draw.line(surf, (255,255,255), (p[0][v1][0]+400, p[0][v1][1]+400), (p[0][v2][0]+400, p[0][v2][1]+400))
            screen.blit(surf, (0,0))
            pygame.display.flip()
            print([p[0][v2][0], p[0][v2][1]])

def rotate(d, ux, uz, pivx, pivz):
    r= py(0, ux-pivx, uz-pivz)
    a= deg(acos((d/2)/r))
    a2= 90-a
    z=d*cos(rad(a2))
    x=d*sin(rad(a2))
    return [ux+x, uz+z, (uz-pivz)/(ux-pivx)]



while True:
    event, val= window.Read()
    for gevent in pygame.event.get():
        if gevent.type == pygame.QUIT: 
            exit('Bye!')

    if event == 's':
        try:
            dims= [int(val['x']),int(val['y']),int(val['z'])] #cube dims xyz\n
            pc= [int(val['ux']),int(val['uy']),int(val['uz'])] #perspective coordinates\n
            pa= [int(val['d']), int(val['ax']), int(val['ay'])] #perspective angles\n
            start= [0,0,0]
            render()
        except:
            print('error risen')
    elif event == 'f':
        form= not form
        try:
            render()
        except:
            print('error risen')

    elif event == 'r':
        rot= rotate(5, pc[0], pc[2], dims[0]/2, dims[2]/2)
        pc= [rot[0], pc[1], rot[1]]
        pa=[pa[0], rot[2], pa[2]]
        render()