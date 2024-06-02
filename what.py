from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def init():
    glClearColor(1,1,1,0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-10,10,-10,10,-100,100)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    # Add draw instructions here
    glPushMatrix()
    glTranslatef(-5,0,0)
    glBegin(GL_QUADS)
    glColor3f(1,0,0); glVertex2f( 5, 5)
    glColor3f(1,1,1); glVertex2f(-5, 5)
    glColor3f(0,0,0); glVertex2f(-5,-5)
    glColor3f(0,0,0); glVertex2f( 5,-5)
    glEnd()
    glPopMatrix()
    glPushMatrix()
    glTranslatef(5,0,0)
    glBegin(GL_POLYGON)
    glColor3f(1,0,0); glVertex2f( 5, 5)
    glColor3f(1,1,1); glVertex2f(-5, 5)
    #glColor3f(0,0,0); glVertex2f(-5,-5)
    glColor3f(0,0,0); glVertex2f( 5,-5)
    glEnd()
    glPopMatrix()
    glFlush()

def main():
    global a,b
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("What's the story?")
    init()
    glutDisplayFunc(display)
    glutMainLoop()
    return

main()
