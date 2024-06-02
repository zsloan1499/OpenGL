from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
from PIL import Image as Image
import time

textID   = 0
img      = []
img_data = []
dX       = 10
sX       = 1
mX       = 0

def init():
    glClearColor(1., 1., 1., 1.)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0,500,0,500,-1,1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def readTextures():
    global textID,img,img_data
    img.append(Image.open("Mario_1.jpg"))
    img_data.append(list(img[textID].getdata()))
    textID += 1
    img.append(Image.open("Mario_2.jpg"))
    img_data.append(list(img[textID].getdata()))
    textID += 1
    img.append(Image.open("Mario_1.jpg"))
    img_data.append(list(img[textID].getdata()))
    textID += 1
    img.append(Image.open("Mario_3.jpg"))
    img_data.append(list(img[textID].getdata()))
    textID += 1
    img.append(Image.open("Pipe.jpg"))
    img_data.append(list(img[textID].getdata()))
    
def drawTile(img):
    glBegin(GL_QUADS);
    glTexCoord2f(1.0, 1.0); glVertex3f(           0,            0, 0.0);
    glTexCoord2f(0.0, 1.0); glVertex3f( img.size[0],            0, 0.0);
    glTexCoord2f(0.0, 0.0); glVertex3f( img.size[0],  img.size[1], 0.0);
    glTexCoord2f(1.0, 0.0); glVertex3f(           0,  img.size[1], 0.0);
    glEnd()

def drawMario(ID):
    global dX, sX, mX
    setTexture(ID)
    glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    mX += dX
    glTranslatef(mX,0,0)
    glScalef(sX,1,1)
    drawTile(img[ID])
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)
    if((mX <= 0)|(mX >= 500-img[ID].size[0])):
        dX = -dX
        sX = -sX

def drawPipe():
    setTexture(4)
    glEnable(GL_TEXTURE_2D)
    glPushMatrix()
    glTranslate(250-img[4].size[0]/2,0,0)
    drawTile(img[4])
    glPopMatrix()
    glDisable(GL_TEXTURE_2D)

def display_scene():
    global textID, dX, sX, mX
    glClear(GL_COLOR_BUFFER_BIT)
    drawPipe()
    textID = (textID + 1) % 4
    drawMario(textID)
    glFlush()
    glutSwapBuffers()
    time.sleep(0.1)

def setTexture(textID):
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)
    glBindTexture(GL_TEXTURE_2D, textID)
    glPixelStorei(GL_UNPACK_ALIGNMENT, 1) 
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB,
                 img[textID].size[0], img[textID].size[1], 0, GL_RGB,
                 GL_UNSIGNED_BYTE, img_data[textID])
    return

def jump( key, x , y ):
    if key == 32:
        
        pass


def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(500, 500)
    glutInitWindowPosition(100, 100)
    glutCreateWindow("Sprite Animation")
    glutDisplayFunc(display_scene)
    glutIdleFunc(display_scene)
    glutKeyboardFunc(jump)
    init()
    readTextures()
    glutMainLoop()

main()

