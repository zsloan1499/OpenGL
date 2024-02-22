import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *



def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 10, 0, 10, -1, 1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glBegin(GL_LINE_LOOP)
    glVertex2d(3,3)
    glVertex2d(5,5)
    glVertex2d(7,2)

    glEnd()

    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Scanline")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()
