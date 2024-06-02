import OpenGL
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image, ImageDraw


texture_id = None

def load_texture():
    global texture_id
    texture_image = Image.open("brick.jpg")
    texture_image = texture_image.transpose(Image.FLIP_TOP_BOTTOM)

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGB, texture_image.width, texture_image.height, 0, GL_RGB, GL_UNSIGNED_BYTE, texture_image.tobytes())


    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)


def init():
    global texture_id
    glClearColor(1, 1, 1, 0)
    glViewport(0, 0, 500, 500)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-25, 25, -25, 25, -25, 25)  # Adjusted viewing volume
    glMatrixMode(GL_MODELVIEW)

    # Set up light source and material properties
    black = [1.0, 0.0, 0.0, 1.0]
    cyan = [1.0, 1.0, 1.0, 1.0]
    white = [1.0, 1.0, 1.0, 1.0]
    light_position = [5.0, 10.0, 5.0, 1.0]  # New position of the light source

    glLightfv(GL_LIGHT0, GL_AMBIENT, black)
    glLightfv(GL_LIGHT0, GL_DIFFUSE, cyan)
    glLightfv(GL_LIGHT0, GL_SPECULAR, white)
    glLightfv(GL_LIGHT0, GL_POSITION, light_position)  # Set light position

    glEnable(GL_LIGHTING)    # Enable lighting
    glEnable(GL_LIGHT0)      # Enable light source 0

    sample = [
        [0.1, 0.9, 0.027451, 1],
        [0.9, 0.9, 0.9, 1],
        [0.9, 0.9, 0.9, 1],
        80]
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT, sample[0])
    glMaterialfv(GL_FRONT_AND_BACK, GL_DIFFUSE, sample[1])
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, sample[2])
    glMaterialf(GL_FRONT_AND_BACK, GL_SHININESS, sample[3])

    load_texture() 

def drawCube(size):
    glBindTexture(GL_TEXTURE_2D, texture_id)


    glBegin(GL_QUADS)
    # Front face
    glColor3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(-size, -size, size)
    glTexCoord2f(1, 0); glVertex3f(size, -size, size)
    glTexCoord2f(1, 1); glVertex3f(size, size, size)
    glTexCoord2f(0, 1); glVertex3f(-size, size, size)
    glEnd()

    # Back face
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f(-size, size, -size)
    glTexCoord2f(1, 1); glVertex3f(size, size, -size)
    glTexCoord2f(0, 1); glVertex3f(size, -size, -size)
    glEnd()

    # Top face
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(-size, size, -size)
    glTexCoord2f(1, 0); glVertex3f(-size, size, size)
    glTexCoord2f(1, 1); glVertex3f(size, size, size)
    glTexCoord2f(0, 1); glVertex3f(size, size, -size)
    glEnd()

    # Bottom face
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f(size, -size, -size)
    glTexCoord2f(1, 1); glVertex3f(size, -size, size)
    glTexCoord2f(0, 1); glVertex3f(-size, -size, size)
    glEnd()

    # Right face
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f(size, size, -size)
    glTexCoord2f(1, 1); glVertex3f(size, size, size)
    glTexCoord2f(0, 1); glVertex3f(size, -size, size)
    glEnd()

    # Left face
    glBegin(GL_QUADS)
    glColor3f(1, 0, 0)
    glTexCoord2f(0, 0); glVertex3f(-size, -size, -size)
    glTexCoord2f(1, 0); glVertex3f(-size, -size, size)
    glTexCoord2f(1, 1); glVertex3f(-size, size, size)
    glTexCoord2f(0, 1); glVertex3f(-size, size, -size)
    glEnd()



def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(10, 10, 10, 0, 0, 0, 0, 1, 0)

    drawCube(10) 

    glutSwapBuffers()




def main():
    glutInit(())
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Static Cube")
    init()
    glutDisplayFunc(display)
    glEnable(GL_DEPTH_TEST)
    glutMainLoop()


main()
