import math
import time

from random import *
from random import randint

import numpy as np

def calculateSetAnimationSteps(selectedObj, xBound, yBound):
    xLength = 0
    yLength = 0
    
    if selectedObj.x > (1000 / 2):
        xLength = selectedObj.x
    if selectedObj.x < (1000 / 2):
        xLength = (xBound - selectedObj.x)

    if selectedObj.y > (600 / 2):
        yLength = selectedObj.y
    if selectedObj.y < (600 / 2):
        yLength = (yBound - selectedObj.y)

    hypo = math.pow((math.pow(xLength, 2) + math.pow(yLength, 2)), .5)

    return int(hypo)

def calculateNewDeltas(objs, selectedObj):
    selectedObj.setExpansiveDeltas(0, 0)

    for obj in objs:
        if obj.x != selectedObj.x and obj.y != selectedObj.y:
            newDeltaX = (selectedObj.x - obj.x) * -1
            newDeltaY = (selectedObj.y - obj.y) * -1
            
            if newDeltaX > 0 and newDeltaY > 0:
                obj.setExpansiveDeltas(8, 8)
            if newDeltaX < -1 and newDeltaY < -1:
                obj.setExpansiveDeltas(-8, -8)
            if newDeltaX < -1 and newDeltaY > 1:
                obj.setExpansiveDeltas(-8, 8)
            if newDeltaX > 1 and newDeltaY < -1:
                obj.setExpansiveDeltas(8, -8)
            if newDeltaX < -1 and newDeltaY == 0:
                obj.setExpansiveDeltas(-8, 0)
            if newDeltaX == 0 and newDeltaY > 1:
                obj.setExpansiveDeltas(0, 8)
            if newDeltaX > 1 and newDeltaY == 0:
                obj.setExpansiveDeltas(8, 0)
            if newDeltaX == 0 and newDeltaY < -1:
                obj.setExpansiveDeltas(0, -8)

def reverseDeltas(objs, selectedObj):
    for obj in objs:
        oldDeltaX = obj.getExpanDeltaX()
        oldDeltaY = obj.getExpanDeltaY()
        
        revDeltaX = oldDeltaX * -1
        revDeltaY = oldDeltaY * -1
        
        obj.setExpansiveDeltas(revDeltaX, revDeltaY)

    print('REVERSED')
            
def expand(selectedObj):
    newRadius = selectedObj.radius + 10
    selectedObj.setRadius(newRadius)

def close(selectedObj):
    newRadius = selectedObj.radius - 10
    selectedObj.setRadius(newRadius)

def update(bub, maxRadius, objs, state):
    if bub.getRadius() < maxRadius and state == 'expand':
        expand(bub)
        
        for obj in objs:
            obj.expansiveUpdate()
        
        return 'expand'
            
    if bub.getRadius() >= maxRadius and state == 'expanded' or bub.getRadius() >= maxRadius and state == 'expand':
        return 'expanded'

    if bub.getRadius() <= 40:
        return 'closed'      
    
    if bub.getRadius() > 40 and state == 'close':
        close(bub)
        
        for obj in objs:
            obj.expansiveUpdate()
        return 'close'
    
