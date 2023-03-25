import pygame
import PySimpleGUI as sg
from forms import cube, pyramid
from engine import py
from math import cos, sin, acos
from math import degrees as deg
from math import radians as rad
import time

size= (1000,1000)
pygame.init()
events = pygame.event.get()
forms=[cube, pyramid]
form=False
objects= {}
timer= 0

dims= [30,30,30] #cube dims xyz\n
pc= [7,30,7] #perspective coordinates\n
pa= [100,-45,-70] #perspective angles\n
start= [0,0,0]

movementValue= 3
rotationValue= 3

layout= [
    [sg.Text('Name:'), sg.Input('', k='n', size=(6,1)), sg.Button('Delete', k='del')],
    [sg.Text('Dims (xyz):'), sg.Input('5', k='x', size=(3,1)), sg.Input('5',k='y', size=(3,1)), sg.Input('5',k='z', size=(3,1))],
    [sg.Text('Start Pos (xyz):'), sg.Input('5', k='sx', size=(3,1)), sg.Input('5',k='sy', size=(3,1)), sg.Input('5',k='sz', size=(3,1))],
    [sg.Text('UrAt (x,y,z):'), sg.Input('5',k='ux', size=(3,1)), sg.Input('5',k='uy', size=(3,1)), sg.Input('5',k='uz', size=(3,1))],
    [sg.Text('view (d,ax,ay):'), sg.Input('5',k='d', size=(3,1)), sg.Input('5',k='ax', size=(3,1)), sg.Input('5',k='ay', size=(3,1))],
    [sg.Button('Create Cube', k='c'), sg.Button('Create Pyramid', k='p'), sg.Button('Change Pos', k='h')]

]

screen = pygame.display.set_mode(size, pygame.RESIZABLE)

surf= pygame.display.set_mode((1000,1000))
window= sg.Window('3D Engine', layout)

def wait(t):
    global timer
    try:
        time.sleep(t-time.time()+timer)
    except:
        print('Overstressed')


def render():
    for obj in list(objects.keys()):
        screen.fill((0,0,0))
        p= forms[int(form)](dims, pc, pa, start)
        for v1 in p.vertices.keys():
            for v2 in p.vertices[v1]:
                pygame.draw.line(surf, (255,255,255), (p.points[v1][0]+400, p.points[v1][1]+400), (p.points[v2][0]+400, p.points[v2][1]+400))
                screen.blit(surf, (0,0))
    
    pygame.display.flip()

def rotate(d, ux, uz, pivx, pivz):
    r= py(0, ux-pivx, uz-pivz)
    a= deg(acos((d/2)/r))
    a2= 90-a
    z=d*cos(rad(a2))
    x=d*sin(rad(a2))
    return [ux+x, uz+z, (uz-pivz)/(ux-pivx)]



while True:
    event, val= window.Read(timeout=0.1)
    for gevent in pygame.event.get():
        if gevent.type == pygame.QUIT: 
            exit('Bye!')
    timer= time.time()

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
    
    #if 'w' key is pressed, move forward
    if pygame.key.get_pressed()[pygame.K_w]:
        
        pc[0]+=movementValue
        render()

    #if 's' key is pressed, move backward
    if pygame.key.get_pressed()[pygame.K_s]:
        
        pc[0]-=movementValue
        render()

    #if 'a' key is pressed, move left
    if pygame.key.get_pressed()[pygame.K_a]:
        
        pc[2]-=movementValue
        render()

    #if 'd' key is pressed, move right
    if pygame.key.get_pressed()[pygame.K_d]:
        
        pc[2]+=movementValue
        render()

    #if ' ' key is pressed, move up
    if pygame.key.get_pressed()[pygame.K_SPACE]:
        
        pc[1]+=1
        render()

    #if 'CTRL' key is pressed, move down
    if pygame.key.get_pressed()[pygame.K_LCTRL]:
        
        pc[1]-=movementValue
        render()

    #if 'left' key is pressed, rotate left
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        
        pa[1]+=rotationValue
        render()

    #if 'right' key is pressed, rotate right
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        
        pa[1]-=rotationValue
        render()

    #if 'up' key is pressed, rotate up
    if pygame.key.get_pressed()[pygame.K_UP]:
        
        pa[2]+=rotationValue
        render()

    #if 'down' key is pressed, rotate down
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        pa[2]-=rotationValue
        render()

    wait(0.2)