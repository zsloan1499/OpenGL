import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(1,1,1,0)
    glViewport(0,0,1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0,0,10,0,0,0,0,1,0)

def drawCube():
    glBegin(GL_QUADS)
    glColor3f(1,0,1)
    glVertex3f(.5,.5,-.5)
    glVertex3f(-.5,.5,-.5)
    glVertex3f(-.5,.5,-.5)
    glVertex3f(.5,.5,.5)

    glColor3f(1,0,0)
    glVertex3f(.5, -.5, .5)
    glVertex3f(-.5, -.5, .5)
    glVertex3f(-.5, -.5, -.5)
    glVertex3f(.5, -.5, -.5)

    glColor3f(0,0,1)
    glVertex3f(.5, .5, .5)
    glVertex3f(-.5, .5, .5)
    glVertex3f(-.5, -.5, .5)
    glVertex3f(.5, -.5, .5)

    glColor3f(.5,0,.5)
    glVertex3f(.5, -.5, -.5)
    glVertex3f(-.5, -.5, -.5)
    glVertex3f(-.5, .5, -.5)
    glVertex3f(.5, .5, -.5)

    glColor3f(.5,0,0)
    glVertex3f(-.5, .5, .5)
    glVertex3f(-.5, .5, -.5)
    glVertex3f(-.5, -.5, -.5)
    glVertex3f(-.5, -.5, .5)

    glColor3f(0,0,.5)
    glVertex3f(.5, .5, -.5)
    glVertex3f(.5, .5, .5)
    glVertex3f(.5, -.5, .5)
    glVertex3f(.5, -.5, -.5)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    drawCube()
    glFlush()

def mykey(key,x,y):
    if (key == '111'):
        glMatrixMode (GL_PROJECTION)
        glLoadIdentity()
        gluPerspective(60.0,1,1,40)
        glutPostRedisplay()
        print('perspective')
    if (key == '112'):
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        gluLookAt(0,0,10,0,0,0,0,1,0)
        glutPostRedisplay()
        print('ortho')
        



def main():
    #gluOrtho
    #gluPerspective
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(800, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("")
    glutDisplayFunc(display)
    glutMainLoop()
    glutKeyboardFunc(mykey)

main()
