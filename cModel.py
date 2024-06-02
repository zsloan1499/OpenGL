from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from random import *

class cModel:
    def __init__(self,newName):
        self.length    = 1
        self.offset    = [0,0]
        self.rotate    = 0
        self.translate = [0,0]
        self.name      = newName
        self.color     = [0,0,0]
        self.children  = []

    def setColor(self,newColor):
        self.color = newColor

    def setOffset(self,newOffset):
        self.offset = newOffset

    def setRotate(self,newRotate):
        self.rotate = newRotate

    def setLength(self,newSize):
        self.length = newSize

    def addChild(self,newChild):
        self.children.append(newChild)

    def drawBone(self):
        glBegin(GL_LINE_LOOP)
        glVertex2f(0,0)
        glVertex2f(self.length/4,self.length/5)
        glVertex2f(self.length,0)
        glVertex2f(self.length/4,-self.length/5)
        glEnd()

    def draw(self):
        glColor(self.color[0],self.color[1],self.color[2])
        glPushMatrix()
        glTranslatef(self.offset[0],self.offset[1],0)
        glTranslatef(self.translate[0],self.translate[1],0)
        glRotatef(self.rotate,0,0,1)
        glPushMatrix()
        self.drawBone()
        #self.drawBox()
        glPopMatrix()
        for child in self.children:
            child.draw()
        glPopMatrix()
