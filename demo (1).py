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
    glutWireCube(1)
    glFlush()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("")
    glutDisplayFunc(display)
    glutMainLoop()

main()
