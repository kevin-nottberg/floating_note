import pygame
from pygame.locals import *

import math
import time

from random import *
from random import randint

import numpy as np

from BubblesClass import Bubbles

from CollisionAPI import *
from ExpansionAPI import *

import xml.etree.ElementTree as ET

#State List: floating, expanding, closing, noting

AQUA = [1, 255, 255]
RED = [255, 1, 1]

SELECTEDX = 0
SELECTEDY = 0

EXPANSIONSTEPS = 0

SCREENX = 1000
SCREENY = 600
STATE = 'floating'

screen = ''
background = ''

notes = []
activeCircles = []

SELECTEDOBJ = ''

testNoteColor = ''

noteSelected = ''

def init():
        global SCREENX
        global SCREENY
        global STATE
        global screen
        global background
        global activeCircles

        global SELECTEDX
        global SELECETEDY

        global EXPANSIONSTEPS

        SCREENX = 1000
        SCREENY = 600
        STATE = 'floating'

	#Setup file name
        tree = ET.parse('notesData.xml')
        root = tree.getroot()

        notes = []
        numberOfNotes = []

        for note in root.findall('bubble'):
                numberOfNotes.append('')
                bubble = Bubbles(40, randint(2, 20), SCREENX, SCREENY, note.attrib, 'notesData.xml')
                activeCircles.append(bubble)

        checkInitPos(activeCircles)

        pygame.init()
        screen = pygame.display.set_mode((SCREENX, SCREENY))
        pygame.display.set_caption('Bubbly')

        background = pygame.Surface(screen.get_size())
        background = background.convert()
        background.fill((255, 255, 255))

        screen.blit(background, (0,0))
        pygame.display.flip()

def centralFunction():
        global SCREENX
        global SCREENY
        global STATE
        global activeCircles
        global screen
        global background
        global SELECTEDX
        global SELECTEDY
        global EXPANSIONSTEPS

        while 1:
                if STATE == 'floating':
                	floating()
                	time.sleep(0.01)
                	background.fill((255, 255, 255))
                	screen.blit(background, (0,0))

                if STATE == 'expansion':
                	expansion()
                	time.sleep(0.0001)
                	background.fill((255, 255, 255))
                	screen.blit(background, (0,0))

                if STATE == 'closing':
                	closing()
                	time.sleep(0.0001)
                	background.fill((255, 255, 255))
                	screen.blit(background, (0,0))

                if STATE == 'noting':
                	noting()
                	time.sleep(0.001)
                	screen.blit(background, (0,0))

def floating():
        global SCREENX
        global SCREENY
        global STATE
        global screen
        global background
        global activeCircles
        global testNoteColor
        global SELECTEDX
        global SELECTEDY
        global EXPANSIONSTEPS
        global SELECTEDOBJ

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        quit()
                        return
                if event.type == MOUSEBUTTONDOWN:
                        print("Click")
                        mousePos = pygame.mouse.get_pos()
                        if STATE == 'floating':
                                if checkClick(mousePos[0], mousePos[1], activeCircles) == True:
                                        SELECTEDX = mousePos[0]
                                        SELECTEDY = mousePos[1]
                                        for bub in activeCircles:
                                                if (SELECTEDX >= (bub.getX() - bub.getRadius())
                                                    and SELECTEDX <= (bub.getX() + bub.getRadius())
                                                    and SELECTEDY >= (bub.getY() - bub.getRadius())
                                                    and SELECTEDY <= (bub.getY() + bub.getRadius())):
                                                        calculateNewDeltas(activeCircles, bub)
                                                        EXPANSIONSTEPS = calculateSetAnimationSteps(bub,
                                                                                                    SCREENX,
                                                                                                    SCREENY)
                                                        SELECTEDOBJ = bub
                                        STATE = 'expansion'

        for bub in activeCircles:
                pygame.draw.circle(background, AQUA, (int(bub.getX()),
                                                      int(bub.getY())), bub.getRadius(), 5)

                bub.checkBounds()
                bub.update()

        collisionHandler(activeCircles)
        screen.fill([0, 100, 150, 100])
        screen.blit(background, (0,0))
        pygame.display.flip()

def expansion():
        global SCREENX
        global SCREENY
        global STATE
        global screen
        global background
        global activeCircles
        global SELECTEDX
        global SELECTEDY
        global EXPANSIONSTEPS
        global SELECTEDOBJ

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        quit()

        expand(SELECTEDOBJ)

        STATE = stateUpdate(STATE, SELECTEDOBJ, EXPANSIONSTEPS, activeCircles)

        for bub in activeCircles:
                pygame.draw.circle(background, AQUA, (int(bub.getX()),
                                                      int(bub.getY())), bub.getRadius(), 5)

        screen.blit(background, (0,0))
        pygame.display.flip()

def closing():
        global SCREENX
        global SCREENY
        global STATE
        global screen
        global background
        global activeCircles
        global SELECTEDX
        global SELECTEDY
        global EXPANSIONSTEPS
        global SELECTEDOBJ

        for event in pygame.event.get():
                if event.type == QUIT:
                        pygame.quit()
                        quit()

        close(SELECTEDOBJ)

        STATE = stateUpdate(STATE, SELECTEDOBJ, EXPANSIONSTEPS, activeCircles)

        for bub in activeCircles:
                pygame.draw.circle(background, AQUA,(int(bub.getX()),
                                                     int(bub.getY())), bub.getRadius(), 5)

        screen.blit(background, (0,0))
        pygame.display.flip()

def noting():
        global SCREENX
        global SCREENY
        global STATE
        global screen
        global background
        global activeCircles
        global SELECTEDX
        global SELECTEDY
        global EXPANSIONSTEPS
        global SELECTEDOBJ
        global testNoteColor
        global noteSelected

        keys = []

        HeaderFont = pygame.font.SysFont('Arial', 30)
        NoteFont = pygame.font.SysFont('Arial', 16)

        events = pygame.event.get()

        for event in events:
                if event.type == QUIT:
                        pygame.quit()
                        quit()

                if event.type == MOUSEBUTTONDOWN:
                        mousePos = pygame.mouse.get_pos()

                        for note in SELECTEDOBJ.getNoteList():
                                NoteFont = pygame.font.SysFont(note.getFont(), note.getTextSize())
                                widthOfNote = NoteFont.size(note.getNoteText())[0]
                                heightOfNote = NoteFont.size(note.getNoteText())[1]

                                x = note.getPosition()[0]
                                y = note.getPosition()[1]
                                if (mousePos[0] >= x and mousePos[0] <= (x + widthOfNote)
                                    and mousePos[1] >= y and mousePos[1] <= (y + heightOfNote)
                                    and note.isSelected() == False):
                                        pygame.draw.line(background, (0, 0, 0), [x, y + heightOfNote],
                                                         [x + widthOfNote + 20, y + heightOfNote], True)

                                        note.selected()

                                elif STATE == 'noting':
                                        if(note.isSelected() == True):
                                                note.deselect()
                                                background.fill((255, 255, 255))
                                        elif(note.isSelected() == False):
                                                STATE = 'closing'
                                                reverseDeltas(activeCircles, SELECTEDOBJ)

                if event.type == MOUSEMOTION:
                        mousePos = pygame.mouse.get_pos()

                        for note in SELECTEDOBJ.getNoteList():
                                NoteFont = pygame.font.SysFont(note.getFont(), note.getTextSize())
                                widthOfNote = NoteFont.size(note.getNoteText())[0]
                                heightOfNote = NoteFont.size(note.getNoteText())[1]

                                x = note.getPosition()[0]
                                y = note.getPosition()[1]
                                if (mousePos[0] >= x and mousePos[0] <= (x + widthOfNote)
                                    and mousePos[1] >= y and mousePos[1] <= (y + heightOfNote)
                                    and note.isSelected() == False):
                                        note.setColor((1, 255, 255))

                                else:
                                        note.setColor((0, 0, 0))

                if event.type == KEYDOWN:
                        for note in SELECTEDOBJ.getNoteList():
                                if note.isSelected():
                                        note.update(events)

        header = SELECTEDOBJ.getHeader()
        noteHeader = HeaderFont.render(header.getNoteText(), True, header.getColor())

        screen.blit(background, (0, 0))

        for note in SELECTEDOBJ.getNoteList():
                widthOfNote = NoteFont.size(note.getNoteText())[0]
                heightOfNote = NoteFont.size(note.getNoteText())[1]
                if note.isSelected() == True:
                     pygame.draw.line(screen, (0, 0, 0), [30, 75 + heightOfNote],
                                [30 + widthOfNote + 20, 75 + heightOfNote], True)

                noteItem1 = NoteFont.render(note.getNoteText(), True, note.getColor())
                screen.blit(noteItem1, note.getPosition())
        screen.blit(noteHeader, header.getPosition())
        pygame.display.flip()

def checkClick(mosX, mosY, objs):
    for click in objs:
        if (mosX <= click.getX() + click.radius and mosX >= click.getX() - click.radius
                and mosY <= click.getY() + click.radius and mosY >= click.getY() - click.radius):
            return True

    return False

def stateUpdate(currState, selectedObj, animationSteps, objs):
        if (selectedObj.getRadius() < animationSteps
            and currState == 'expansion'):
                expand(selectedObj)

                for obj in objs:
                        obj.expansiveUpdate()

                return 'expansion'

        if (selectedObj.getRadius() > 40
            and currState == 'closing'):
                close(selectedObj)

                for obj in objs:
                        obj.expansiveUpdate()

                return 'closing'

        if (selectedObj.getRadius() >= animationSteps
            and currState == 'expansion'):
                return 'noting'

        if (selectedObj.getRadius() <= 40
            and currState == 'closing'):
                return 'floating'


if __name__ == '__main__':
	init()
	centralFunction()
