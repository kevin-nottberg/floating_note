import OpenGL.GL as gl
from simple_vector_library import *

class Note:
    def __init__(self, header, headerSize, headerFont,
                    text, textSize, textColor, textFont):
        self.pos = Py_Vector(0, 0)

        self.header = header
        self.headerSize = headerSize
        self.headerFont = headerFont

        self.text = text
        self.textSize = getText
        self.textColor = textColor
        self.textFont = textFont
