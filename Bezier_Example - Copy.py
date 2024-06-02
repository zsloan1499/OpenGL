from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *

ctrlpoints = [[-100,0,0],[50,50,0],[-50,50,0],[100,0,0]]

h3 = 100
w3 = 50
is_dragging = False
tX = 0
tY = 0
mX = 0
mX = 0
 
def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glViewport(0, 0, 500,500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250.0, 250.0, -250.0 , 250.0 , -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def drawSquare(pt):
    x = 5
    glColor3f(1,1,0)
    glBegin(GL_POLYGON)
    glVertex2f(pt[0]-x,pt[1]-x)
    glVertex2f(pt[0]-x,pt[1]+x)
    glVertex2f(pt[0]+x,pt[1]+x)
    glVertex2f(pt[0]+x,pt[1]-x)
    glEnd()
    
def draw(ctrlpoints):
    glMap1f(GL_MAP1_VERTEX_3, 0.0, 1.0, ctrlpoints)
    glEnable(GL_MAP1_VERTEX_3)
    glColor3f(1.0, 1.0, 1.0)
    glBegin(GL_LINE_STRIP)
    for i in range(30):
        glEvalCoord1f(i / 30.0) 
    glEnd()
    for i in range(4):
        drawSquare(ctrlpoints[i])
    glFlush()
    glutSwapBuffers()

    
def display():
    draw(ctrlpoints)
 
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if (w <= h):
        glOrtho(-250.0, 250.0, -250.0 * h / w, 250.0 * h / w, -5.0, 5.0)
    else:
        glOrtho(-250.0 * w / h, 250.0 * w / h, -250.0, 250.0, -5.0, 5.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def mouse(button, state, x, y):
    global is_dragging, mX, mY, tX, tY
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        distance = 
        if distance <= 10:
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
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(501, 501)
    glutInitWindowPosition(80,80)
    glutCreateWindow("Bezier Example")
    init()
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    glutMainLoop()

main()
