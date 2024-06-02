from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def drawWirePoly(n, r):
    glBegin(GL_LINE_LOOP)
    glColor3f(0, 1, 0)
    for i in range(n):
        theta = 2.0 * 3.1415926 * i / n
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2f(x, y)
    glEnd()

def drawWireStar(r_outer, r_inner):
    glBegin(GL_LINE_LOOP)
    glColor3f(.5, .5, .5)
    glVertex2f(.45, -.27)
    for i in range(5):
        theta_outer = 2.0 * 3.1415926 * i / 5
        x_outer = r_outer * cos(theta_outer)
        y_outer = r_outer * sin(theta_outer)
        glVertex2f(x_outer, y_outer)

        theta_inner = theta_outer + (3.1415926 / 5)  # Adjust angle for inner vertex
        x_inner = r_inner * cos(theta_inner)
        y_inner = r_inner * sin(theta_inner)
        glVertex2f(x_inner, y_inner)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 1)  # change color

    # Draw wireframe polygon
    glLoadIdentity()
    glRotatef(90, 0, 0, 1)
    drawWirePoly(10, 1)
 

    # Draw wireframe star inside the circle
    drawWireStar(1, 0.5)  # Outer radius is 1, Inner radius is 0.5

    glutSwapBuffers()

def init():
    glClearColor(1, 1, 1, 0)
    glViewport(0, 0, 500, 500)  # Adjust the viewport size

def main():
    glutInit()
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("")
    glutDisplayFunc(draw)
    glutMainLoop()

main()