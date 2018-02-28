import pygame
from pygame.locals import *

import math
import time

from random import *
from random import randint

import numpy as np

from BubblesClass import Bubbles

def collisionHandler(objs):
    k = 0
    while k < len(objs):
        i = 0
        while i < len(objs):
            if objs[k].getX() == objs[i].getX() and objs[k].getY() == objs[i].getY():
                break
            else:
                distance = getDistance(objs[k], objs[i])
                if distance <= objs[k].radius + objs[i].radius:
                    #resolveCollision2(obj[k], obj[i])
                    resolveCollision3(objs[k], objs[i])
            i = i + 1
        k = k + 1

def getDistance(obj1, obj2):
    xDistance = obj2.x - obj1.x
    yDistance = obj2.y - obj1.y

    d = math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))
    return d

def resolveCollision2(ball1, ball2):
    d = math.sqrt(pow(ball1.x - ball2.x, 2) + pow(ball1.y - ball2.y, 2))

    #normalized x and y
    nx = (ball2.x - ball1.x) / d
    ny = (ball2.y - ball1.y) / d
    
    p = 2 * (ball1.deltaX * nx + ball1.deltaY * ny - ball2.deltaX * nx - ball2.deltaY * ny) / (2)

    vx1 = (ball1.deltaX - p * ball1.mass * nx)
    vy1 = (ball1.deltaY - p * ball1.mass * ny)

    vx2 = (ball2.deltaX - p * ball2.mass * nx)
    vy2 = (ball2.deltaY - p * ball2.mass * ny)

    ball1.setDeltas(vx1, vy1)
    ball2.setDeltas(vx2, vy2)

    print("collision2")

def resolveCollision3(ball1, ball2):

    newVelXBall1 = (ball1.deltaX * (ball1.mass - ball2.mass) + (2 * ball2.mass * ball2.deltaX)) / (ball1.mass + ball2.mass)
    newVelYBall1 = (ball1.deltaY * (ball1.mass - ball2.mass) + (2 * ball2.mass * ball2.deltaY)) / (ball1.mass + ball2.mass)

    newVelXBall2 = (ball2.deltaX * (ball2.mass - ball1.mass) + (2 * ball1.mass * ball1.deltaX)) / (ball1.mass + ball2.mass)
    newVelYBall2 = (ball2.deltaY * (ball2.mass - ball1.mass) + (2 * ball1.mass * ball1.deltaY)) / (ball1.mass + ball2.mass)

    ball1.setDeltas(newVelXBall1, newVelYBall1)
    ball2.setDeltas(newVelXBall2, newVelYBall2)

def checkInitPos(objs):
    allPositions = []
    for circle in objs:
        allPositions.append(circle.getPosition())
        
    k = 0
    while k < len(objs):
        i = 0
        while i < len(objs):
            if objs[k].getX() == objs[i].getX() and objs[k].getY() == objs[i].getY():
                break
            else:
                distance = getDistance(objs[k], objs[i])
                if distance <= objs[k].radius + objs[i].radius:
                    while distance <= objs[k].getRadius() + objs[i].getRadius():
                        xK = randint(40, 960)
                        yK = randint(40, 540)

                        xI = randint(40, 960)
                        yI = randint(40, 960)

                        objs[k].setPosition((xK, yK)) 
                    
                        objs[i].setPosition((xI, yI))

                        distance = getDistance(objs[k], objs[i])
            i = i + 1
        k = k + 1
