import math
import numpy as np
import time

from random import *
from random import randint

from Bubble import Bubble

def collisionHandler(objs):
    for bubble in objs:
        for bubble2 in objs:
            if(bubble.ID == bubble2.ID):
                break
            else:
                if getDistance(bubble, bubble2) <= bubble.radius + bubble2.radius:
                    resolveCollision4(bubble, bubble2)


def getDistance(obj1, obj2):
    xDistance = obj2.pos.x_component - obj1.pos.x_component
    yDistance = obj2.pos.y_component - obj1.pos.y_component

    return math.sqrt(math.pow(xDistance, 2) + math.pow(yDistance, 2))

def resolveCollision3(ball1, ball2):
    newVelXBall1 = ((ball1.vel.x_component * (ball1.mass - ball2.mass) 
                    + (2 * ball2.mass * ball2.vel.x_component)) / (ball1.mass + ball2.mass))
    newVelYBall1 = ((ball1.vel.x_component * (ball1.mass - ball2.mass)
                    + (2 * ball2.mass * ball2.vel.x_component)) / (ball1.mass + ball2.mass))

    newVelXBall2 = ((ball2.vel.x_component * (ball2.mass - ball1.mass)
                    + (2 * ball1.mass * ball1.vel.x_component)) / (ball1.mass + ball2.mass))
    newVelYBall2 = ((ball2.vel.x_component * (ball2.mass - ball1.mass)
                    + (2 * ball1.mass * ball1.vel.x_component)) / (ball1.mass + ball2.mass))

    ball1.vel.x_component = newVelXBall1
    ball1.vel.y_component = newVelYBall1

    ball2.vel.x_component = newVelXBall2
    ball2.vel.y_component = newVelYBall2

def resolveCollision4(obj1, obj2):
    xDistance = obj2.pos.x_component - obj1.pos.x_component
    yDistance = obj2.pos.y_component - obj1.pos.y_component
    
    deltaXVel = obj2.vel.x_component - obj1.vel.x_component
    deltaYVel = obj2.vel.y_component - obj1.vel.y_component

    vx_cm = (obj1.mass * obj1.vel.x_component + obj2.mass * obj2.vel.x_component)/(obj1.mass + obj2.mass)
    vy_cm = (obj1.mass * obj1.vel.y_component + obj2.mass * obj2.vel.y_component)/(obj1.mass + obj2.mass)

    if(deltaXVel == 0.0):
        deltaXVel = 1
    a = deltaYVel / deltaXVel
    dvx2 = -2*(deltaXVel + a * deltaYVel)/((1 + a * a)*(1+(obj2.mass/obj1.mass)))

    obj2.vel.x_component = obj2.vel.x_component + dvx2
    obj2.vel.y_component = obj2.vel.y_component + a * dvx2

    obj1.vel.x_component = obj1.vel.x_component - (obj2.mass/obj1.mass)*dvx2
    obj1.vel.y_component = obj1.vel.y_component - a * (obj2.mass/obj1.mass) * dvx2
                                        
    

