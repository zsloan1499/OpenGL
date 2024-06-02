from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from cModel import *

def init():
    global model1, model2, model3
    glClearColor(1,1,1,0)
    glMatrixMode(GL_PROJECTION);  
    glLoadIdentity()
    #glOrtho(-50,50,-50,50,-100,10)
    gluPerspective(60.0, 1.0, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW);  
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 85.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.)

    model1 = cModel("Lower Spine")
    model1.setColor([0,1,0])
    model1.setLength(8)
    model1.setOffset([0,-11])
    model1.setRotate(90)
    model2 = cModel("Middle Spine")
    model2.setColor([0,0,1])
    model2.setLength(8)
    model2.setOffset([9,0])
    model2.setRotate(0)
    model3 = cModel("Upper Spine")
    model3.setColor([0,1,1])
    model3.setLength(8)
    model3.setOffset([9,0])
    model3.setRotate(0)
    model4 = cModel("Neck")
    model4.setColor([0,1,1])
    model4.setLength(3)
    model4.setOffset([7,0])
    model4.setRotate(0)
    model5 = cModel("Head")
    model5.setColor([0,1,1])
    model5.setLength(8)
    model5.setOffset([3,0])
    model5.setRotate(0)
    model6 = cModel("Right Arm")
    model6.setColor([0,1,1])
    model6.setLength(8)
    model6.setOffset([8,-1])
    model6.setRotate(-90)
    model7 = cModel("Left arm")
    model7.setColor([0,1,1])
    model7.setLength(8)
    model7.setOffset([8,1])
    model7.setRotate(90)
    model1.addChild(model2)
    model2.addChild(model3)
    model3.addChild(model4)#Neck
    model4.addChild(model5)#Head
    model3.addChild(model6)#Right Arm
    model3.addChild(model7)#Left Arm


def display():
    global model1
    glClear(GL_COLOR_BUFFER_BIT)
    # Add draw instructions here
    glColor3f(1,0,0)
    glBegin(GL_LINES)
    glVertex3f(-50,0,0)
    glVertex3f(50,0,0)
    glVertex3f(0,-50,0)
    glVertex3f(0,50,0)
    glEnd()
    glColor3f(0,0,0)
    glPushMatrix()
    #glutWireCube(1)
    model1.draw()
    glPopMatrix()
    glFlush()

def main():
    global a,b
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Articulated Model Example")
    init()
    glutDisplayFunc(display)
    glutMainLoop()

main()
