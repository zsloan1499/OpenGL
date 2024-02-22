import math

import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# store vertices
vertices = []

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    glPointSize(5)
    glBegin(GL_POINTS)
    for vertex in vertices:
        glVertex2f(vertex[0], vertex[1])
    glEnd()

    if len(vertices) >= 2:
        glColor3f(0, 0, 0)
        glBegin(GL_LINE_STRIP)
        for vertex in vertices:
            glVertex2f(vertex[0], vertex[1])
        glEnd()
        # draws line segment between vertices
        if len(vertices) > 0:
            glColor3f(0, 0, 0)
            glBegin(GL_LINES)
            glVertex2f(vertices[-1][0], vertices[-1][1])
            glVertex2f(mouse_x, 500 - mouse_y)
            glEnd()

    glFlush()

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

def mouse(button, state, x, y):
    global mouse_x, mouse_y
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        # are we ending the polygon?
        if len(vertices) >= 2 and distance((x, 500 - y), vertices[0]) <= 10:
            vertices.append(vertices[0])  # Close the polygon
        else:
            vertices.append((x, 500 - y))
        glutPostRedisplay()
    mouse_x, mouse_y = x, y

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Mouse Polygon")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMainLoop()

main()