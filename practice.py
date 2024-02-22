import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Global variables to track mouse position and drawing state
mouse_x = 0
mouse_y = 0
drawing = False

# List to store points of the drawn curve
curve_points = []

def init():
    glClearColor(1, 1, 1, 0)
    glViewport(0, 0, 500, 500)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(0, 0, 0)
    
    # Draw existing curve
    glBegin(GL_LINE_STRIP)
    for point in curve_points:
        glVertex2f(point[0], point[1])
    glEnd()
    
    glFlush()

def mouse(button, state, x, y):
    global drawing
    if button == GLUT_LEFT_BUTTON:
        if state == GLUT_DOWN:
            drawing = True
            # Start drawing a new curve, clear existing points
            curve_points.clear()
        elif state == GLUT_UP:
            drawing = False
            # End drawing of the curve, curve is completed
            glutPostRedisplay()

def motion(x, y):
    global mouse_x, mouse_y
    if drawing:
        # Add the current mouse position to the curve points
        curve_points.append((x, 500 - y))
        glutPostRedisplay()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Draw Curves")
    glutDisplayFunc(display)
    glutMouseFunc(mouse)
    glutMotionFunc(motion)
    init()
    glutMainLoop()

main()