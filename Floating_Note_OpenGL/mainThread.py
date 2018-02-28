#! /usr/bin/env python

import pygame
import pygame_textinput
from datetime import datetime
import numpy as np
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from Bubble import *
from CollisionAPI import *
from ExpansionAPI import *
import global_settings as gls

global circles, numOfNotes, initialRadius, STATE, textInput, clock
textInput = pygame_textinput.TextInput()
clock = pygame.time.Clock()
circles = []

numOfNotes = 10
initialRadius = 45
STATE = 'floating'

def enviromentSetup():
    global circles, numOfNotes, initialRadius

    for i in range(numOfNotes):
        bub = Bubble(initialRadius, 100, i, 2000)
        bub.pos.x_component = (i+1) * ((gls.SCREENWIDTH - (initialRadius + initialRadius/2))/numOfNotes)
        bub.pos.y_component = randint(initialRadius, gls.SCREENHEIGHT - initialRadius)
        circles.append(bub)

    pygame.init()
    display = (gls.SCREENWIDTH, gls.SCREENHEIGHT)
    #pygame.display.set_mode(display, DOUBLEBUF|RESIZABLE|OPENGL)
    pygame.display.set_mode(display, OPENGLBLIT)

    gluOrtho2D(0, gls.SCREENWIDTH, 0, gls.SCREENHEIGHT)
    glShadeModel(GL_SMOOTH)

def main():
    global circles, STATE

    bg_red = 0
    bg_green = 0
    bg_blue = 255
    bg_state = 'red'

    while True:
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
        glClearColor(RGBtoFloat(5), RGBtoFloat(127), RGBtoFloat(232), RGBtoFloat(150))

        if STATE == 'floating':
            floating()

        if STATE == 'expansion':
            expansion()

        if STATE == 'closing':
            closing()

        if STATE == 'noting':
            noting()

        glFinish()

        '''
        if(bg_state == 'red'):
            bg_red += 1
            bg_blue -= 1
            if(bg_red > 255):
                bg_state = 'green'
        if(bg_state == 'green'):
            bg_green += 1
            bg_red -= 1
            if(bg_green > 255):
                bg_state = 'blue'
        if(bg_state == 'blue'):
            bg_blue += 1
            bg_green -= 1
            if(bg_blue > 255):
                bg_state = 'red'
        '''

        pygame.display.flip()
        pygame.time.wait(10)

def floating():
    global circles, STATE, selectedCircle, expansionRadius, initialRadius

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == MOUSEBUTTONDOWN:
            selectedCircle = checkClick(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], circles)
            if(selectedCircle != False):
                calculateExpansiveDeltas(circles, selectedCircle, 30)
                expansionRadius = hypoRadiusCorner(selectedCircle, gls.SCREENWIDTH, gls.SCREENHEIGHT)
                #Set the state to expansion to start the update process of that
                STATE = 'expansion'

    #Draw call's here
    for bubble in circles:
        bubble.draw()
        bubble.update('floating')

    collisionHandler(circles)

def expansion():
    global circles, STATE, selectedCircle, expansionRadius

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == MOUSEBUTTONDOWN:
            reverseExpansiveDeltas(circles)
            STATE = 'closing'

    expand(selectedCircle)

    for circle in circles:
        if(circle.ID != selectedCircle.ID):
            circle.draw()
            circle.update('expansion')
        else:
            selectedCircle.expansiveDraw()
    if(selectedCircle.radius > expansionRadius):
        STATE = 'noting'

def closing():
    global circles, STATE, selectedCircle, expansionRadius, initialRadius

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            quit()

    close(selectedCircle)

    for circle in circles:
        if(circle.ID != selectedCircle.ID):
            circle.draw()
            circle.update('expansion')
        else:
            selectedCircle.expansiveDraw()

    if(selectedCircle.radius <= initialRadius):
        STATE = 'floating'
        for circle in circles:
            circle.pos = Py_Vector(circle.preExpansivePos.x_component,
                                    circle.preExpansivePos.y_component)

def noting():
    global circle, STATE, textInput, clock

    events = pygame.event.get()
    for event in events:
        if event.type == QUIT:
            pygame.quit()
            quit()

        if event.type == MOUSEBUTTONDOWN:
            reverseExpansiveDeltas(circles)
            STATE = 'closing'
            
    textInput.update(events)
    pygame.display.get_surface().blit(textInput.get_surface(), (10,10))
    clock.tick(30)


def screenResize():
    x = 1

def RGBtoFloat(rgbColor):
    return rgbColor / 255

def checkClick(mouseX, mouseY, objs):
    global circles

    mouseY = gls.SCREENHEIGHT - mouseY
    for obj in objs:
        if(mouseX <= obj.pos.x_component + obj.radius
            and mouseX >= obj.pos.x_component - obj.radius
                and mouseY <= obj.pos.y_component + obj.radius
                    and mouseY >= obj.pos.y_component - obj.radius):

            return obj

    print('false')
    return False


if __name__ == '__main__':
    enviromentSetup()
    main()
