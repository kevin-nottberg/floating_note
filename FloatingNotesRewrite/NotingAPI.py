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
        
        for event in pygame.event.get():
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
                        keys = pygame.key.get_pressed()

                if event.type == KEYDOWN:
                        keys = pygame.key.get_pressed()


                #print(keys)

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
