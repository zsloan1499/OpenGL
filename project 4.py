from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from PIL import Image

vertices = [
    (0.5, -0.5, 0.5),   
    (-0.5, -0.5, 0.5),  
    (-0.5, -0.5, -0.5), 
    (0.5, -0.5, -0.5),  
    (0, 0.5, 0)        
]


polygons = [
    (0, 1, 2),  #
    (0, 2, 3),  
    (0, 3, 4),  
    (0, 4, 1),  
    (1, 2, 4),  
    (2, 3, 4),  
    (3, 0, 4),  
    (0, 1, 4)   
]

texture_coords = [
    (0.5, 0.0),  
    (0.0, 0.0), 
    (0.0, 0.5), 
    (0.5, 0.5), 
    (0.5, 1.0)  
]

def load_texture(texture_path):
    img = Image.open(texture_path)
    img_data = img.convert("RGBA").tobytes("raw", "RGBA", 0, -1)
    width, height = img.size
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA, GL_UNSIGNED_BYTE, img_data)
    return texture

def init():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_TEXTURE_2D)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glEnable(GL_COLOR_MATERIAL)
    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 0.0, 1.0, 0.0))  
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.5, 0.5, 0.5, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))
    glLightfv(GL_LIGHT0, GL_SPECULAR, (1.0, 1.0, 1.0, 1.0))

def draw_pyramid():
    glBindTexture(GL_TEXTURE_2D, load_texture("cinder-block.jpg"))
    glBegin(GL_TRIANGLES)
    for i, polygon in enumerate(polygons):
        for vertex_index in polygon:
            vertex = vertices[vertex_index]
            texture_coord = texture_coords[vertex_index]
            glTexCoord2fv(texture_coord)
            glVertex3fv(vertex)
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    gluPerspective(45, (800/600), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)
    glRotatef(60, .1, 1, 0)  # Rotate for a better view
    draw_pyramid()
    glutSwapBuffers()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)
    glutInitWindowSize(800, 600)
    glutCreateWindow("Pyramid with Lighting and Texture")
    glutDisplayFunc(display)
    init()
    glutMainLoop()

if __name__ == "__main__":
    main()
