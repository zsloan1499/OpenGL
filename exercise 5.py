from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Initial window size and camera position
width, height = 500, 500
camera_y = 0
camera_x = 0
is_ortho = True  # Projection type flag

def setup_viewport():
    global camera_y
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    if is_ortho:
        # Orthographic projection setup
        glOrtho(-2.0, 2.0, -2.0, 2.0, 2.0, 10.0)
    else:
        # Perspective projection setup
        gluPerspective(45, (width / height), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(camera_x, camera_y, -5, 0, 0, 0, 0, 1, 0)  # Camera position and orientation

def draw_cube():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glutWireCube(2)  # Draw the cube
    glFlush()  # Flush commands to ensure all commands are executed

def key_pressed(key, x, y):
    global is_ortho

    if key in [b'o', b'O']:
        is_ortho = True
    elif key in [b'p', b'P']:
        is_ortho = False

    setup_viewport()
    glutPostRedisplay()

def special_keys(key, x, y):
    global camera_y
    global camera_x

    if key == GLUT_KEY_UP:
        camera_y += 0.5  # Move camera up
    elif key == GLUT_KEY_DOWN:
        camera_y -= 0.5  # Move camera down
    elif key == GLUT_KEY_LEFT:
        camera_x -= 0.5  # Move camera down
    elif key == GLUT_KEY_RIGHT:
        camera_x += 0.5  # Move camera down

    setup_viewport()
    glutPostRedisplay()

def main():
    global width, height

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_RGBA | GLUT_SINGLE | GLUT_DEPTH)  # Use single buffering
    glutInitWindowSize(width, height)
    glutCreateWindow(b"OpenGL Cube with Camera Control - Single Buffer")

    glutDisplayFunc(draw_cube)
    glutKeyboardFunc(key_pressed)
    glutSpecialFunc(special_keys)

    glEnable(GL_DEPTH_TEST)

    setup_viewport()

    glutMainLoop()

if __name__ == "__main__":
    main()