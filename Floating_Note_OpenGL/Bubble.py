from simple_vector_library import Py_Vector
import numpy as np
import math
from random import *
import global_settings as gls

from OpenGL.GL import *
from OpenGL.GLU import *

class Bubble:
    def __init__(self, radius, mass, ID, resolution):
        #self.pos = Py_Vector(randint(radius, gls.SCREENWIDTH - radius), randint(radius, gls.SCREENHEIGHT - radius))
        self.pos = Py_Vector(0, 0)
        self.vel = Py_Vector(randint(-5, 5), randint(-4, 4))
        self.accel = Py_Vector(0, 0)

        self.resolution = resolution

        self.preExpansivePos = Py_Vector(0, 0)
        self.expansiveVelocity = Py_Vector(0, 0)

        self.radius = radius
        self.mass = mass

        self.ID = ID

        self.noteList = []

        self.vertList = []
        self.shineVertList = []
        self.calculateVerticies()

    '''
    def draw(self):
        glLineWidth(4)
        glBegin(GL_LINE_LOOP)
        for i in range(self.resolution):
            theta = 2.0 * 3.1415926 * i/self.resolution
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            glVertex2f(self.pos.x_component + x, self.pos.y_component + y)
        glEnd()

        #Bubble shine
        glBegin(GL_LINE_LOOP)
        for i in range(math.ceil(self.resolution/8)):
            theta = 2.0 * 3.1415926 * i/(self.resolution)
            x = (self.radius * 0.75) * np.cos(theta)
            y = (self.radius * 0.75) * np.sin(theta)
            glVertex2f(self.pos.x_component + x, self.pos.y_component + y)
        glEnd()
    '''

    def draw(self):
        glLineWidth(5)
        glBegin(GL_LINE_LOOP)
        for i in range(0, len(self.vertList,), 2):
            glVertex2f(self.pos.x_component + self.vertList[i],
                        self.pos.y_component + self.vertList[i + 1])

        glEnd()

        glBegin(GL_LINE_LOOP)
        for i in range(0, len(self.shineVertList), 2):
            glVertex2f(self.pos.x_component + self.shineVertList[i],
                        self.pos.y_component + self.shineVertList[i + 1])
        glEnd()

    def calculateVerticies(self):
        for i in range(self.resolution):
            theta = 2.0 * 3.1415926 * (i/self.resolution)
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            self.vertList.append(math.ceil(x))
            self.vertList.append(math.ceil(y))

        for i in range(math.ceil(self.resolution/8)):
            theta = 2.0 * 3.145926 * i/(self.resolution)
            x = (self.radius * 0.75) * math.cos(theta)
            y = (self.radius * 0.75) * math.sin(theta)
            self.shineVertList.append(math.ceil(x))
            self.shineVertList.append(math.ceil(y))


    def update(self, STATE):
        if(STATE == 'floating'):
            #this.vel.add(this.accel)
            self.pos.add(self.vel)
            if(self.pos.x_component >= gls.SCREENWIDTH - (self.radius + 3)):
                self.vel.x_component *= -1
                self.pos.x_component = (gls.SCREENWIDTH - (self.radius + 3))

            if(self.pos.x_component <= self.radius + 3):
                self.vel.x_component *= -1
                self.pos.x_component = (self.radius + 3)

            if(self.pos.y_component >= gls.SCREENHEIGHT - (self.radius+3)):
                self.vel.y_component *= -1
                self.pos.y_component = (gls.SCREENHEIGHT - (self.radius + 3))

            if(self.pos.y_component <= self.radius+3):
                self.vel.y_component *= -1
                self.pos.y_component = (self.radius + 3)
        elif(STATE == 'expansion'):
            self.pos.add(self.expansiveVelocity)
        elif(STATE == 'closing'):
            self.pos.sub(self.expansiveVelcoity)

        self.vel.limit(5)

    def expansiveDraw(self):
        glLineWidth(4)
        glBegin(GL_LINE_LOOP)
        for i in range(self.resolution):
            theta = 2.0 * 3.1415926 * i/self.resolution
            x = self.radius * math.cos(theta)
            y = self.radius * math.sin(theta)
            glVertex2f(self.pos.x_component + x, self.pos.y_component + y)
        glEnd()

        #Removing the shine as the bubbles are bouncing speeds up
        # the expansion animation
        '''
        #Bubble shine
        glBegin(GL_TRIANGLES)
        for i in range(math.ceil(self.resolution/8)):
            theta = 2.0 * 3.1415926 * i/(self.resolution)
            x = (self.radius * 0.75) * np.cos(theta)
            y = (self.radius * 0.75) * np.sin(theta)
            glVertex2f(self.pos.x_component + x, self.pos.y_component + y)
        glEnd()
        '''
