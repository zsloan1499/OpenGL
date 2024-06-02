from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

purple = [[0.8, 0.8, 0.027451, 1],
            [0.780392, 0.568627, 0.113725, 1],
            [0.992157, 0.941176, 0.807843, 1],
            27.8974]
    




def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()

    # Rotate the scene so we can see the tops of the shapes.
    glRotatef(-20.0, 1.0, 0.0, 0.0)

    glMaterialfv(GL_FRONT, GL_AMBIENT, purple[0])
    glMaterialfv(GL_FRONT, GL_DIFFUSE, purple[1])
    glMaterialfv(GL_FRONT, GL_SPECULAR, purple[2])
    glMaterialf(GL_FRONT, GL_SHININESS, purple[3])

    glPushMatrix()
    glutSolidSphere(1.0, 30, 30)
    glPopMatrix()

    glPopMatrix()
    glFlush()
    
def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    aspect = w / h
    glLoadIdentity()
    if (w <= h):
        glOrtho(-2.5, 2.5, -2.5/aspect, 2.5/aspect, -10.0, 10.0)
    else:
        glOrtho(-2.5*aspect, 2.5*aspect, -2.5, 2.5, -10.0, 10.0)

def init():
    glClearColor(1,1,1,0)
    black = [ 1.0, 0.0, 0.0, 1.0 ]
    yellow = [ 1.0, 1.0, 0.0, 1.0 ]
    cyan = [ 1.0, 1.0, 1.0, 1.0 ]
    white = [ 1.0, 1.0, 1.0, 1.0 ]
    direction = [ 1.0, 1.0, 1.0, 0.0 ]


    glLightfv(GL_LIGHT0, GL_AMBIENT, black)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, cyan)
    glLightfv(GL_LIGHT0, GL_SPECULAR, white)
    glLightfv(GL_LIGHT0, GL_POSITION, direction)

    glEnable(GL_LIGHTING)              # so the renderer considers light
    glEnable(GL_LIGHT0)                 # turn LIGHT0 on
    glEnable(GL_DEPTH_TEST)             # so the renderer considers depth

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowPosition(80, 80)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Cyan Shapes in Yellow Light")
    glutReshapeFunc(reshape)
    glutDisplayFunc(display)
    init()
    glutMainLoop()

main()
