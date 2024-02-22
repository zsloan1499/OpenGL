from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

def drawWirePoly(n, r):
    glBegin(GL_LINE_LOOP)
    for i in range(n):
        theta = 2.0 * 3.1415926 * i / n
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2f(x, y)
    glEnd()

def drawSolidPoly(n, r):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(0, 0)  # Center of the polygon
    for i in range(n + 1):
        theta = 2.0 * 3.1415926 * i / n
        x = r * cos(theta)
        y = r * sin(theta)
        glVertex2f(x, y)
    glEnd()

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 1, 1)  # Set color to white

    # Draw filled polygon
    #glLoadIdentity()
    #drawSolidPoly(6, 0.5)

    #Draw wireframe polygon
    glLoadIdentity()
    drawWirePoly(12, 0.5)

    glutSwapBuffers()

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1.0, 1.0, -1.0, 1.0)
    glMatrixMode(GL_MODELVIEW)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("OpenGL Window")
    glutDisplayFunc(draw)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()