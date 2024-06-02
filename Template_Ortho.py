from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def drawCircle(R,cX,cY):
    steps = 1000
    glBegin(GL_LINE_LOOP)
    for i in range(steps):
        angle = 2 * pi * i / steps
        x = cX + R * cos(angle)
        y = cY + R * sin(angle)
        glVertex2f(x,y)
    glEnd()

def init():
    glClearColor(1,1,1,0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-1,1,-1,1,-1,10)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    # Add draw instructions here
    drawCircle(.5,0,0)
    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
    return

main()
