import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *


def init():
    glClearColor(1,1,0,0)
    glViewport(0,0,1,1)
    

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)

def mouseClick(button,state,x,y):
    if button == GLUT_LEFT_BUTTON:
        while button == GLUT_DOWN:
            glColor3f(1,0,1)
            glVertex2f(x,y)
            print("works")

def motion(x,y):
    pass

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouseClick)
    glutMotionFunc(motion)
    glutMainLoop()

main()
