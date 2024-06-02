import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

left_ball_y = 0.0
right_ball_y = 0.0
time = 0
y2 = 0
acc = 0
vel = 0
rad = 0
maxY = 0
dt = 1
period = 0
frame = 0

def init():
    glClearColor(1, 1, 1, 0)
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-2, 2, -2, 2, -1, 1)

def display():
    global left_ball_y, right_ball_y, time
    
    glClear(GL_COLOR_BUFFER_BIT)
    glColor3f(1, 0, 0)

    # left ball
    left_ball_y = math.sin(time) * 1.25  # Amplitude of 0.5
    glPushMatrix()
    glTranslatef(-1, left_ball_y, 0)
    glutWireSphere(.75, 20, 20)
    glPopMatrix()

    #right ball
    if right_ball_y > 0.01 :  # where it hits "ground"
        right_ball_y += 0.05  
    elif right_ball_y < -1 :
        right_ball_y -= 0.05
    else:
        right_ball_y -= 0.05
    glPushMatrix()
    glTranslatef(1, right_ball_y, 0)
    glutWireSphere(.75, 20, 20)
    glPopMatrix()

    glutSwapBuffers()

def update(value):
    global time
    time += 0.1  # sin curve time
    glutPostRedisplay()
    glutTimerFunc(30, update, 0)

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Bouncing Balls")
    glutDisplayFunc(display)
    glutTimerFunc(25, update, 0)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
