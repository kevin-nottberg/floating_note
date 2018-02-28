import numpy as np
import math
from random import *

class Py_Vector:
    def __init__(self, x = 0, y = 0, z = 0):
        self.x_component = x
        self.y_component = y
        self.z_component = z

    def copy(self):
        return(Py_Vector(self.x_component, self.y_component, self.z_component))

    def add(self, x, y=0, z=0):
        if(isinstance(x, Py_Vector)):
            self.x_component += x.x_component
            self.y_component += x.y_component
            self.z_component += x.z_component

        elif(isinstance(x, (np.ndarray, np.generic, list, tuple))):
            self.x_component += x[0]
            self.y_component += x[1]
            if(len(x) == 3):
                self.z_component += x[2]

        else:
            self.x_component += x
            self.y_component += y
            self.z_component += z

    def sub(self, x, y=0, z=0):
        if(isinstance(x, Py_Vector)):
            self.x_component -= x.x_component
            self.y_component -= x.y_component
            self.z_component -= x.z_component

        elif(isinstance(x, (np.ndarray, np.generic, list, tuple))):
            self.x_component -= x[0]
            self.y_component -= x[1]
            if(len(x) == 3):
                self.z_component -= x[2]

        else:
            self.x_component -= x
            self.y_component -= y
            self.z_component -= z

    def multi(self, scale):
        self.x_component *= scale
        self.y_component *= scale
        self.z_component *= scale

    def div(self, n):
        if(n == 0):
            print("Can't divide by zero")

        self.x_component /= n
        self.y_component /= n
        self.z_component /= n

    def mag(self):
        return math.sqrt(self.x_component * self.x_component
                        + self.y_component * self.y_component
                        + self.z_component * self.z_component)

    def dot(self, x, y=0, z=0):
        if(isinstance(x, Py_Vector)):
            return (self.x_component * x.x_component
                    + self.y_component * x.y_component
                    + self.z_component * x.z_component)

        return (self.x_component * x
                + self.y_component * y
                + self.z_component * z)


    def cross(self, vector):
        cross_x = (self.y_component * vector.z_component
                    - self.z_component * vector.y_component)
        cross_y = (self.z_component * vector.x_component
                    - self.x_component * vector.z_component)
        cross_z = (self.x_component * vector.y_component
                    - self.y_component * vector.x_component)

        return Py_Vector(cross_x, cross_y, cross_z)

    def dist(self, vector):
        return vector.copy.sub(self).mag()

    def normalize(self):
        if self.mag == 0:
            return self
        else:
            return self.div(self.mag())

    def limit(self, max):
        mSq = (self.x_component * self.x_component
                        + self.y_component * self.y_component
                        + self.z_component * self.z_component)
        if(mSq > max * max):
            self.div(math.sqrt(mSq))
            self.multi(max)

        return self

    def setMag(self, n):
        return self.normalize().multi(n)

    def heading(self):
        #Returns radians
        h = math.atan2(self.y_component, self.x_component)
        return h

    def rotate(self, a):
        newHeading = self.heading + a
        mag = self.mag()
        self.x_component = math.cos(newHeading) * setMag
        self.y_component = math.sin(newHeading) * setMag
        return self

    def angleBetween(self, vector):
        dotmagmag = self.dot(vector) / (self.mag() * vector.mag())
        angle = math.acos(min(1, max(-1, dotmagmag)))
        return angle
