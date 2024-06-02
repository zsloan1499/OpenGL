from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys
from PIL import Image as Image

textID = 0

def init():
    glClearColor(0., 0., 0., 1.)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-250,250,-250,250,-1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def drawSquare():
    glBegin(GL_QUADS);
    glTexCoord2f(0.0, 0.0); glVertex3f(-100.0, -100.0,  0.0);
    glTexCoord2f(1.0, 0.0); glVertex3f( 100.0, -100.0,  0.0);
    glTexCoord2f(1.0, 1.0); glVertex3f( 100.0,  100.0,  0.0);
    glTexCoord2f(0.0, 1.0); glVertex3f(-100.0,  100.0,  0.0);
    glEnd()

def display_scene():
    glClear(GL_COLOR_BUFFER_BIT)
    read_texture("grass.jpg")
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glTranslatef(-100,0,0)
    drawSquare()
    glPopMatrix()
    glFlush()
    glDisable(GL_TEXTURE_2D)
    read_texture("brick.jpg")
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    #glBindTexture(GL_TEXTURE_2D, 2)
    glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glTranslatef(100,0,0)
    drawSquare()
    glPopMatrix()
    glFlush()
    glDisable(GL_TEXTURE_2D)


def read_texture(filename):
    global textID
    #textID += 1
    img = Image.open(filename)
    img_data = list(img.getdata())
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, img.size[0], img.size[1], 0, GL_RGB,
                 GL_UNSIGNED_BYTE, img_data)
    return textID


def changeTexture(key, x, y):
    global textID
    textID += 1
    if ( key == b'32' and textID == 1):
        textID +=1
    elif (key == b'32' and textID == 2):
        textID -= 1
    return textID

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(501, 501)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Multiple Textures Example")
    glutDisplayFunc(display_scene)
    glutKeyboardFunc(changeTexture)
    init()
    glutMainLoop()

main()

