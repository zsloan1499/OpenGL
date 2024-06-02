from PIL import Image, ImageDraw
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

def init():
    glClearColor(1, 1, 1, 1)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 500, 0, 500, -1, 1)

def drawTexture():
    image = Image.new("RGB", (256, 256), "white")
    draw = ImageDraw.Draw(image)
    
    draw.rectangle([0, 0, 255, 255], fill="red")

    draw.ellipse([20, 20, 50, 50], fill="white")
    draw.ellipse([120, 20, 150, 50], fill="white")

    draw.ellipse([70, 60, 100, 90], fill="white")
    draw.ellipse([170, 60, 200, 90], fill="white")

    draw.ellipse([20, 100, 50, 130], fill="white")
    draw.ellipse([120, 100, 150, 130], fill="white")

    draw.ellipse([70, 140, 100, 170], fill="white")
    draw.ellipse([170, 140, 200, 170], fill="white")

    draw.ellipse([20, 180, 50, 210], fill="white")
    draw.ellipse([120, 180, 150, 210], fill="white")

    draw.ellipse([70, 220, 100, 250], fill="white")
    draw.ellipse([170, 220, 200, 250], fill="white")

    image_data = image.tobytes("raw", "RGBX", 0, -1)
    image_width, image_height = image.size

    return image_data, image_width, image_height

def load_texture():
    image_data, image_width, image_height = drawTexture()

    texture_id = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture_id)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, image_width, image_height, 0, GL_RGBA, GL_UNSIGNED_BYTE, image_data)
    return texture_id

def draw_cube(texture_id):
    glBindTexture(GL_TEXTURE_2D, texture_id)

    # Front face
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, 1.0)
    glEnd()

    # Back face
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)
    glEnd()

    # Right face
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(1.0, 1.0, 1.0)
    glEnd()

    # Left face
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(-1.0, -1.0, 1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)
    glEnd()

    # Top face
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(1.0, 1.0, 1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(1.0, 1.0, -1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, 1.0, -1.0)
    glEnd()

    # Bottom face
    glBegin(GL_QUADS)
    glTexCoord2f(0.0, 0.0); glVertex3f(-1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 0.0); glVertex3f(1.0, -1.0, -1.0)
    glTexCoord2f(1.0, 1.0); glVertex3f(1.0, -1.0, 1.0)
    glTexCoord2f(0.0, 1.0); glVertex3f(-1.0, -1.0, 1.0)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)
    draw_cube(texture_id)
    glutSwapBuffers()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, width/height, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit(())
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(500, 500)
    glutCreateWindow("Polka Dot Cube")
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    global texture_id
    texture_id = load_texture()
    glutMainLoop()

if __name__ == "__main__":
    main()
