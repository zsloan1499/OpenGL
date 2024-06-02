from OpenGL import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from math import *
from cModel3 import *



def init():
    global pelvis
    glClearColor(0,0,0,0)
    glMatrixMode(GL_PROJECTION);  
    glLoadIdentity()
    #glOrtho(-50,50,-50,50,-100,10)
    gluPerspective(60.0, 1.0, 1.0, 100.0)
    glMatrixMode(GL_MODELVIEW);  
    glLoadIdentity()
    gluLookAt(0.0, 0.0, 85.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0)


    pelvis = cModel3("Pelvis",3,[0,0,300])
    pelvis.setOffset([0, 13, 0])

    #rotate spine kind of like image idk its weird to replicate how he is sitting
    spine3 = cModel3("Spine 3",10,[30,0,115])
    pelvis.addChild(spine3)
    #since we flipped the pelvis we have to move the spine out the pelvis so we offset it
    spine3.setOffset([0, 0, 0])

#neck
    neck = cModel3(" Neck ",2,[0,0,150])
    neck.setColor([0.5,1,0.5])
    spine3.addChild(neck)

#head
    head = cModel3(" Head ",7,[0,0,160])
    head.setColor([0.5,0.5,1])
    neck.addChild(head)



#right arm
    rShoulder = cModel3("Right Shoulder",4,[0,0,275])
    rShoulder.setColor([1,0.5,0.5])
    spine3.addChild(rShoulder)
    
    upperRArm = cModel3("Upper Right Arm",7,[0,0,270])
    upperRArm.setColor([1,0.5,0.5])
    rShoulder.addChild(upperRArm)
    
    lowerRArm = cModel3("Lower Right Arm",6,[0,0,230])
    lowerRArm.setColor([1,0.5,0.5])
    upperRArm.addChild(lowerRArm)
    
    rHand = cModel3("Right Hand",2,[0,0,290])
    rHand.setColor([1,0.5,0.5])
    lowerRArm.addChild(rHand)

#left arm
    lShoulder = cModel3("Left Shoulder",3,[0,0,230])
    lShoulder.setColor([0,0,1])
    spine3.addChild(lShoulder)
    
    upperLArm = cModel3("Upper Left Arm",10,[0,0,265])
    upperLArm.setColor([0,0,1])
    lShoulder.addChild(upperLArm)
    
    lowerLArm = cModel3("Lower Left Arm",10,[0,0,110])
    lowerLArm.setColor([0,0,1])
    upperLArm.addChild(lowerLArm)
    
    LHand = cModel3("Left Hand",4,[0,0,60])
    LHand.setColor([0,0,1])
    lowerLArm.addChild(LHand)

#right leg
    UpperRLeg = cModel3("Upper Right Leg",12,[0,-40,210])
    UpperRLeg.setColor([0,1,0])
    pelvis.addChild(UpperRLeg)

    RKnee = cModel3("Right Knee",2,[0,0,300])
    RKnee.setColor([0,1,0])
    UpperRLeg.addChild(RKnee)
    
    lowerRLeg = cModel3("Lower Right Leg",8,[0,0,290])
    lowerRLeg.setColor([0,1,0])
    RKnee.addChild(lowerRLeg)
    
    rFoot = cModel3("Right Foot",5,[0,220,330])
    rFoot.setColor([0,1,0])
    lowerRLeg.addChild(rFoot)

#left leg

    UpperLLeg = cModel3("Upper Left Leg",14,[0,0,200])
    UpperLLeg.setColor([0.5,0,5,0.5])
    pelvis.addChild(UpperLLeg)

    LKnee = cModel3("Left Knee",2,[0,0,290])
    LKnee.setColor([0.5,0,5,0.5])
    UpperLLeg.addChild(LKnee)

    lowerLLeg = cModel3("Lower Left Leg",10,[0,0,290])
    lowerLLeg.setColor([0.5,0,5,0.5])
    LKnee.addChild(lowerLLeg)
    
    lFoot = cModel3("Left Foot",5,[0,80,220])
    lFoot.setColor([0.5,0,5,0.5])
    lowerLLeg.addChild(lFoot)
    


    """
    
    upperRArm = cModel3("Upper Right Arm",10,[0,0,180])
    upperRArm.setColor([1,0,0])
    spine3.addChild(upperRArm)
    
    lowerRArm = cModel3("Lower Right Arm",10,[0,0,180])
    lowerRArm.setColor([0,1,0])
    upperRArm.addChild(lowerRArm)
    
    rHand = cModel3("Right Hand",5,[0,0,180])
    rHand.setColor([0,0,1])
    lowerRArm.addChild(rHand)
    """


def display():
    global model1
    glClear(GL_COLOR_BUFFER_BIT)
    # Add draw instructions here
    glColor3f(1,1,0)
    glutWireCube(13)
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
    pelvis.draw()
    glPopMatrix()
    glFlush()
    glutSwapBuffers()

def main():
    global a,b
    glutInit(())
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Articulated Model Example")
    init()
    glutDisplayFunc(display)
    glutIdleFunc(display)
    glutMainLoop()

main()
