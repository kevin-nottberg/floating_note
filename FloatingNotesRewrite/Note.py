import pygame
from pygame.locals import *

import math
import time

from random import *
from random import randint

class Note():
    
    def __init__(self, x, y, text):
        self.STATE = 'NOTSELECTED'
        self.x = x
        self.y = y
        self.originalText = text
        self.currText = self.originalText
        self.color = (0, 0, 0)
        self.shifted = False
        
    def setPosition(self, x, y):
        self.x = x
        self.y = y
        
    def getPosition(self):
        return(self.x, self.y)

    def setNoteText(self, text):
        curr.text = text
    
    def getNoteText(self):
        return self.currText

    def setTextSize(self, size):
        self.textSize = size

    def getTextSize(self):
        return self.textSize
        
    def setFont(self, font):
        self.font = font

    def getFont(self):
        return self.font

    def update(self, events):
        for event in events:
            if event.type == KEYUP:
                if event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = False
                print('True')
            if event.type == KEYDOWN:
                if event.key == K_BACKSPACE: self.currText = self.currText[:-1]
                elif event.key == K_LSHIFT or event.key == K_RSHIFT: self.shifted = True
                elif event.key == K_SPACE: self.currText += ' '
                if not self.shifted:
                    if event.key == K_a: self.currText += 'a'
                    elif event.key == K_b: self.currText += 'b'
                    elif event.key == K_c: self.currText += 'c'
                    elif event.key == K_d: self.currText += 'd'
                    elif event.key == K_e: self.currText += 'e'
                    elif event.key == K_f: self.currText += 'f'
                    elif event.key == K_g: self.currText += 'g'
                    elif event.key == K_h: self.currText += 'h'
                    elif event.key == K_i: self.currText += 'i'
                    elif event.key == K_j: self.currText += 'j'
                    elif event.key == K_k: self.currText += 'k'
                    elif event.key == K_l: self.currText += 'l'
                    elif event.key == K_m: self.currText += 'm'
                    elif event.key == K_n: self.currText += 'n'
                    elif event.key == K_o: self.currText += 'o'
                    elif event.key == K_p: self.currText += 'p'
                    elif event.key == K_q: self.currText += 'q'
                    elif event.key == K_r: self.currText += 'r'
                    elif event.key == K_s: self.currText += 's'
                    elif event.key == K_t: self.currText += 't'
                    elif event.key == K_u: self.currText += 'u'
                    elif event.key == K_v: self.currText += 'v'
                    elif event.key == K_w: self.currText += 'w'
                    elif event.key == K_x: self.currText += 'x'
                    elif event.key == K_y: self.currText += 'y'
                    elif event.key == K_z: self.currText += 'z'
                    elif event.key == K_0: self.currText += '0'
                    elif event.key == K_1: self.currText += '1'
                    elif event.key == K_2: self.currText += '2'
                    elif event.key == K_3: self.currText += '3'
                    elif event.key == K_4: self.currText += '4'
                    elif event.key == K_5: self.currText += '5'
                    elif event.key == K_6: self.currText += '6'
                    elif event.key == K_7: self.currText += '7'
                    elif event.key == K_8: self.currText += '8'
                    elif event.key == K_9: self.currText += '9'
                    elif event.key == K_BACKQUOTE: self.currText += '`'
                    elif event.key == K_MINUS: self.currText += '-'
                    elif event.key == K_EQUALS: self.currText += '='
                    elif event.key == K_LEFTBRACKET: self.currText += '['
                    elif event.key == K_RIGHTBRACKET: self.currText += ']'
                    elif event.key == K_BACKSLASH: self.currText += '\\'
                    elif event.key == K_SEMICOLON: self.currText += ';'
                    elif event.key == K_QUOTE: self.currText += '\''
                    elif event.key == K_COMMA: self.currText += ','
                    elif event.key == K_PERIOD: self.currText += '.'
                    elif event.key == K_SLASH: self.currText += '/'
                elif self.shifted == True:
                    if event.key == K_a: self.currText += 'A'
                    elif event.key == K_b: self.currText += 'B'
                    elif event.key == K_c: self.currText += 'C'
                    elif event.key == K_d: self.currText += 'D'
                    elif event.key == K_e: self.currText += 'E'
                    elif event.key == K_f: self.currText += 'F'
                    elif event.key == K_g: self.currText += 'G'
                    elif event.key == K_h: self.currText += 'H'
                    elif event.key == K_i: self.currText += 'I'
                    elif event.key == K_j: self.currText += 'J'
                    elif event.key == K_k: self.currText += 'K'
                    elif event.key == K_l: self.currText += 'L'
                    elif event.key == K_m: self.currText += 'M'
                    elif event.key == K_n: self.currText += 'N'
                    elif event.key == K_o: self.currText += 'O'
                    elif event.key == K_p: self.currText += 'P'
                    elif event.key == K_q: self.currText += 'Q'
                    elif event.key == K_r: self.currText += 'R'
                    elif event.key == K_s: self.currText += 'S'
                    elif event.key == K_t: self.currText += 'T'
                    elif event.key == K_u: self.currText += 'U'
                    elif event.key == K_v: self.currText += 'V'
                    elif event.key == K_w: self.currText += 'W'
                    elif event.key == K_x: self.currText += 'X'
                    elif event.key == K_y: self.currText += 'Y'
                    elif event.key == K_z: self.currText += 'Z'
                    elif event.key == K_0: self.currText += ')'
                    elif event.key == K_1: self.currText += '!'
                    elif event.key == K_2: self.currText += '@'
                    elif event.key == K_3: self.currText+= '#'
                    elif event.key == K_4: self.currText += '$'
                    elif event.key == K_5: self.currText += '%'
                    elif event.key == K_6: self.currText += '^'
                    elif event.key == K_7: self.currText += '&'
                    elif event.key == K_8: self.currText += '*'
                    elif event.key == K_9: self.currText += '('
                    elif event.key == K_BACKQUOTE: self.currText += '~'
                    elif event.key == K_MINUS: self.currText += '_'
                    elif event.key == K_EQUALS: self.currText += '+'
                    elif event.key == K_LEFTBRACKET: self.currText += '{'
                    elif event.key == K_RIGHTBRACKET: self.currText += '}'
                    elif event.key == K_BACKSLASH: self.currText += '|'
                    elif event.key == K_SEMICOLON: self.currText += ':'
                    elif event.key == K_QUOTE: self.currText += '"'
                    elif event.key == K_COMMA: self.currText += '<'
                    elif event.key == K_PERIOD: self.currText += '>'
                    elif event.key == K_SLASH: self.currText += '?'
        
    def isSelected(self):
        if self.STATE == 'NOTSELECTED':
            return False
        if self.STATE == 'SELECTED':
            return True

    def save(self):
        self.originalText = self.currText

    def selected(self):
        self.STATE = 'SELECTED'

    def deselect(self):
        self.STATE = 'NOTSELECTED'

    def setColor(self, color):
        self.color = color
        
    def getColor(self):
        return self.color


    
    
        
    
    
