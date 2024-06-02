from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from cModel import *

# Global variables for animation
angle_upper_arm = 0
angle_lower_arm = 0
angle_hand = 0
angle_direction = 1

def init():
    global model1, model2, model3
    glClearColor(1, 1, 1, 0)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(60.0, 1.0, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 85.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)

    model1 = cModel("Upper Arm")
    model1.setColor([0, 1, 0])
    model1.setLength(10)
    model1.setOffset([0, 0])
    model1.setRotate(30)
    model2 = cModel("Lower Arm")
    model2.setColor([0, 0, 1])
    model2.setLength(10)
    model2.setOffset([10, 0])
    model2.setRotate(30)
    model3 = cModel("Hand")
    model3.setColor([0, 1, 1])
    model3.setLength(5)
    model3.setOffset([10, 0])
    model3.setRotate(30)
    model1.addChild(model2)
    model2.addChild(model3)


def update_animation(value):
    global angle_upper_arm, angle_lower_arm, angle_hand, angle_direction

    # Update angles
    angle_upper_arm += angle_direction * 2
    angle_lower_arm += angle_direction * 3
    angle_hand += angle_direction * 4

    # Change direction when reaching limits
    if angle_upper_arm >= 45 or angle_upper_arm <= -45:
        angle_direction *= -1

    glutPostRedisplay()
    glutTimerFunc(30, update_animation, 0)


def display():
    global model1, angle_upper_arm, angle_lower_arm, angle_hand
    glClear(GL_COLOR_BUFFER_BIT)
    
    # Draw coordinate axes
    glColor3f(1, 0, 0)
    glBegin(GL_LINES)
    glVertex3f(-50, 0, 0)
    glVertex3f(50, 0, 0)
    glVertex3f(0, -50, 0)
    glVertex3f(0, 50, 0)
    glEnd()
    
    # Draw arm model
    glColor3f(0, 0, 0)
    glPushMatrix()
    model1.setRotate(angle_upper_arm)
    model2.setRotate(angle_lower_arm)
    model3.setRotate(angle_hand)
    model1.draw()
    glPopMatrix()
    glFlush()


def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Articulated Model Animation")
    init()
    glutDisplayFunc(display)
    glutTimerFunc(30, update_animation, 0)  # Start animation timer
    glutMainLoop()


main()
