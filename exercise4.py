import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(1,1,1,0)
    glViewport(0,0,1,1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1,0,0)
    # Add draw instructions here
    glTranslatef(-.45,-.45,0)
    glRotatef(300, 0, 0, 1)
    glutWireTeapot(.3)

    glLoadIdentity()
    glTranslatef(-.45,.45,0)
    glRotatef(225, 0, 0, 1)
    glutWireTeapot(.3)

    glLoadIdentity()
    glTranslatef(.45,-.45,0)
    glRotatef(45, 0, 0, 1)
    glutWireTeapot(.3)

    glLoadIdentity()
    glTranslatef(.45,.45,0)
    glRotatef(135, 0, 0, 1)
    glutWireTeapot(.3)

    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(800, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("")
    glutDisplayFunc(display)
    glutMainLoop()

main()
