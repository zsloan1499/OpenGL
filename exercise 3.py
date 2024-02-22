from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def drawPoly(arr):
    glBegin(GL_POLYGON)
    glColor3f(1, 1, 1)  #color change
    for element in arr:
        x = element[0]
        y = element[1]
        glVertex2f(x,y)
    glEnd()
    glutSwapBuffers()

def drawWirePoly(arr):
    glBegin(GL_LINE_LOOP)
    glColor3f(1, 0, 1)  #color change
    for element in arr:
        x = element[0]
        y = element[1]
        glVertex2f(x,y)
    glEnd()
    glutSwapBuffers()
    

def draw():
    #create the array
    array = [[.1, .1],[.3, .1],[.1, .5],[.3,.5]]
    glLoadIdentity()
    drawPoly(array)
    drawWirePoly(array)
    


def init():
    glClearColor(1,1,1,0)
    glViewport(0,0,1,1)


def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("")
    glutDisplayFunc(draw)
    glutMainLoop()

main()