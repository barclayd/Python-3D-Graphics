import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),
    (1, 1, -1),
    (-1, 1, -1),
    (-1, -1, -1),
    (0, 0, 1)
)

edges = (
    (0, 1),
    (0, 3),
    (0, 4),
    (1, 4),
    (1, 2),
    (2, 4),
    (2, 3),
    (3, 4)
)


def draw_pyramid():
    glLineWidth(5)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()


def main():
    pygame.init()
    display = (800, 800)
    # set pygame up for 3d graphics
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    # moves back along z direction
    glTranslatef(0, 0, -5)

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

