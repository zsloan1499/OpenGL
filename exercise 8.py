from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

circle_radius = 25
is_dragging = False
tX = 0
tY = 0
mX = 0
mX = 0

def drawCircle(R):
    steps = 1000
    glBegin(GL_LINE_LOOP)
    for i in range(steps):
        angle = 2 * pi * i / steps
        x = R * cos(angle)
        y = R * sin(angle)
        glVertex2f(x, y)
    glEnd()

def init():
    glClearColor(1, 1, 1, 0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-249, 250, -249, 250, -10, 10)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)
    glPushMatrix()
    glTranslatef(tX,tY,0)
    drawCircle(circle_radius)
    glPopMatrix()
    glFlush()

def mouse(button, state, x, y):
    global is_dragging, mX, mY, tX, tY, circle_radius
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        distance = sqrt((x - 249 - tX) ** 2 + (249 - y - tY) ** 2)
        if distance <= circle_radius:
            is_dragging = True
            mX = x
            mY = y
            print("inside")
    elif button == GLUT_LEFT_BUTTON and state == GLUT_UP:
        is_dragging = False

def motion(x, y):
    global is_dragging, mX, mY, tX, tY
    if is_dragging:
        dX = x - mX
        dY = y - mY
        tX += dX
        tY -= dY
        mX = x
        mY = y
        glutPostRedisplay()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("exercise 8")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()
    return

main()
