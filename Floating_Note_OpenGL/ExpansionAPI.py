import math, datetime
from simple_vector_library import *

def hypoRadiusCorner(selectedObj, xBound, yBound):
    xLength = 0
    yLength = 0

    if(selectedObj.pos.x_component > (xBound/2)):
        xLength = selectedObj.pos.x_component
    if(selectedObj.pos.x_component < (xBound/2)):
        xLength = (xBound - selectedObj.pos.x_component)

    if(selectedObj.pos.y_component > (yBound /2)):
        yLength = selectedObj.pos.y_component
    if(selectedObj.pos.y_component < (yBound / 2)):
        yLength = (yBound - selectedObj.pos.y_component)

    return int(math.pow(math.pow(xLength, 2) + math.pow(yLength, 2), .5))


def calculateExpansiveDeltas(objs, selectedObj, expansionRate):
    selectedObj.expansiveVelcoity = Py_Vector(0, 0)

    for obj in objs:
        obj.preExpansivePos = Py_Vector(obj.pos.x_component, obj.pos.y_component)
        if obj.ID != selectedObj.ID:
            deltaX = ((selectedObj.pos.x_component - obj.pos.x_component) * -1)
            deltaY = ((selectedObj.pos.y_component - obj.pos.y_component) * -1)

            obj.expansiveVelocity = Py_Vector(deltaX, deltaY)
            obj.expansiveVelocity.normalize()
            obj.expansiveVelocity.multi(expansionRate)

def reverseExpansiveDeltas(objs):
    for obj in objs:
        obj.expansiveVelocity.x_component *= -1
        obj.expansiveVelocity.y_component *= -1

def expand(selectedObj):
    selectedObj.radius += 30

def close(selectedObj):
    selectedObj.radius -= 30
