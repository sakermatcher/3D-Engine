import pygame
import PySimpleGUI as sg
from forms import preSets
from engine import py
from math import cos, sin, acos
from math import degrees as deg
from math import radians as rad
import time

size= (1000,1000)
pygame.init()
events = pygame.event.get()
objects= {'test':preSets.cube([300,300,300], [0,0,0])}
timer= 0

pc= [5000,150,150]
pa= [300, 0, 0]

movementValue= 3
rotationValue= 3

layout= [
    [sg.Text('Name:'), sg.Input('', k='n', size=(6,1)), sg.Button('Delete', k='del')],
    [sg.Text('Dims (xyz):'), sg.Input('30', k='x', size=(3,1)), sg.Input('30',k='y', size=(3,1)), sg.Input('30',k='z', size=(3,1))],
    [sg.Text('Start Pos (xyz):'), sg.Input('0', k='sx', size=(3,1)), sg.Input('0',k='sy', size=(3,1)), sg.Input('0',k='sz', size=(3,1))],
    [sg.Text('UrAt (x,y,z):'), sg.Input('7',k='ux', size=(3,1)), sg.Input('30',k='uy', size=(3,1)), sg.Input('30',k='uz', size=(3,1))],
    [sg.Text('view (d,ax,ay):'), sg.Input('100',k='d', size=(3,1)), sg.Input('45',k='ax', size=(3,1)), sg.Input('-70',k='ay', size=(3,1))],
    [sg.Button('Create Cube', k='c'), sg.Button('Create Pyramid', k='p'), sg.Button('Change Pos', k='pos')]

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
    global surf
    screen.fill((20,20,20))
    surf.fill((20,20,20))
    for obj in list(objects.values()):
        for pol in obj.polygons:
            surf= pol.render(pc, pa, surf)
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
    event, val= window.Read(timeout=0.001)
    for gevent in pygame.event.get():
        if gevent.type == pygame.QUIT: 
            exit('Bye!')
    timer= time.time()

    if event == 'c':
        try:
            dims= [int(val['x']),int(val['y']),int(val['z'])] #cube dims xyz\n
            start= [int(val['sx']),int(val['sy']),int(val['sz'])]
            objects[val['n']]= preSets.cube(dims, start)
            render()
        except:
            print('error risen')

    if event == 'p':
        try:
            dims= [int(val['x']),int(val['y']),int(val['z'])] #cube dims xyz\n
            start= [int(val['sx']),int(val['sy']),int(val['sz'])]
            objects[val['n']]= preSets.pyramid(dims, start)
            render()
        except:
            print('error risen')

    if event == 'del':
        try:
            del objects[val['n']]
            render()
        except:
            print('error risen')

    elif event == 'pos':
        pc= [int(val['ux']),int(val['uy']),int(val['uz'])] #perspective coordinates\n
        pa= [int(val['d']), int(val['ax']), int(val['ay'])] #perspective angles\n

    elif event == 'r':
        rot= rotate(5, pc[0], pc[2], dims[0]/2, dims[2]/2)
        pc= [rot[0], pc[1], rot[1]]
        pa=[pa[0], rot[2], pa[2]]
        render()
    
    #if 'w' key is pressed, move forward
    if pygame.key.get_pressed()[pygame.K_w]:
        pc[0]+= movementValue*(cos(rad(pa[1])) + 0)
        pc[2]+= movementValue*(sin(rad(pa[1])) + 0)
        render()

    #if 's' key is pressed, move backward
    if pygame.key.get_pressed()[pygame.K_s]:
        pc[0]+= movementValue*(cos(rad(pa[1])) + 180)
        pc[2]+= movementValue*(sin(rad(pa[1])) + 180)
        render()

    #if 'a' key is pressed, move left
    if pygame.key.get_pressed()[pygame.K_a]:
        pc[0]+= movementValue*(cos(rad(pa[1])) + 270)
        pc[2]+= movementValue*(sin(rad(pa[1])) + 270)
        render()

    #if 'd' key is pressed, move right
    if pygame.key.get_pressed()[pygame.K_d]:
        pc[0]+= movementValue*(cos(rad(pa[1])) + 90)
        pc[2]+= movementValue*(sin(rad(pa[1])) + 90)
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
        if pa[1] > 359:
            pa[1]=0
        render()

    #if 'right' key is pressed, rotate right
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        pa[1]-=rotationValue
        if pa[1] < 0:
            pa[1]=359
        render()

    #if 'up' key is pressed, rotate up
    if pygame.key.get_pressed()[pygame.K_UP]:
        pa[2]+=rotationValue
        if pa[2] > 359:
            pa[2]=0
        render()

    if pygame.key.get_pressed()[pygame.K_q]:
        pa[0]+=rotationValue
        render()

    if pygame.key.get_pressed()[pygame.K_e]:
        pa[0]-=rotationValue
        render()

    if pygame.key.get_pressed()[pygame.K_p]:
        print(f'xyz: {pc}, pa: {pa}')

    #if 'down' key is pressed, rotate down
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        pa[2]-=rotationValue
        if pa[2] < 0:
            pa[2]=359
        render()

    wait(0.2)