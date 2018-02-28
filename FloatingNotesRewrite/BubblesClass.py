from random import *

import xml.etree.ElementTree as ET

from Note import *

class Bubbles:
    def __init__(self, size, m, xMax, yMax, ID, xmlFileName):

        self.x = randint(40, 960)
        self.y = randint(40, 560)
        
        self.radius = size
        self.mass = m

        self.xBound = xMax
        self.yBound = yMax

        self.ID = ID

        tree = ET.parse(xmlFileName)
        root = tree.getroot()

        self.noteList = []

        for note in root.findall('bubble'):
            if(note.attrib == self.ID):
                print(note.tag)
                print(self.ID)
                print('true')
                self.header = Note(30, 30, note.find('header').text)
                self.header.setTextSize(30)
                self.header.setFont('Arial')
                self.header.setColor((0, 0, 0))
                contents = Note(30, 75, note.find('text').text)
                contents.setTextSize(16)
                contents.setFont('Arial')
                contents.setColor((0,0,0))
                self.noteList.append(contents)

        self.randomMvmnt()
                

    def setDeltas(self, delX, delY):
        self.deltaX = delX
        self.deltaY = delY

    def setExpansiveDeltas(self, exDelX, exDelY):
        self.expanDelX = exDelX
        self.expanDelY = exDelY

    def getExpanDeltaX(self):
        return self.expanDelX

    def getExpanDeltaY(self):
        return self.expanDelY

    def setRadius(self, size):
        self.radius = size

    def getRadius(self):
        return self.radius

    def getDeltaX(self):
        return self.deltaX

    def getDeltaY(self):
        return self.deltaY

    def update(self):
        if self.deltaX > 10:
            self.deltaX = 6
        if self.deltaX < -10:
            self.deltaX = -6
        if self.deltaY > 10:
            self.deltaX = 6
        if self.deltaY < -10:
            self.deltaY = -6
        self.x = self.x + self.deltaX
        self.y = self.y + self.deltaY
        #self.i = self.i + 1

    def expansiveUpdate(self):
        self.x = self.x + self.expanDelX
        self.y = self.y + self.expanDelY

    def getPosition(self):
        return (self.x, self.y)

    def setPosition(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        
    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def randomMvmnt(self):
        xMovement = randint(-2, 2)
        yMovement = randint(-2, 2)
        self.deltaX = xMovement
        self.deltaY = yMovement
        #self.i = 0
        #self.animationSteps = randint(150, 500)

    def checkSteps(self):
        if self.i == self.animationSteps:
            return True
        else:
            return False
        
    def checkBounds(self):
        if self.x >= (self.xBound - self.radius) or self.x <= (self.radius):
            self.deltaX = self.deltaX * -1
            
        if self.y >= (self.yBound - self.radius) or self.y <= (self.radius):
            self.deltaY = self.deltaY * -1

    def getNumberOfNotes(self):
        return len(self.noteList) - 1
    
    def setNoteText(self, text):
        self.noteText = text

    def getNoteText(self):
        return self.noteText

    def getNoteList(self):
        return self.noteList

    def getText(self):
        return noteText

    def getHeader(self):
        return self.header
