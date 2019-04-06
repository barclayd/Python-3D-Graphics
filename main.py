import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import numpy

# settings

screen_height = 800
screen_width = 800
line_colour = (0, 89, 179)


class Pyramid:
    vertices = [
        [1, -1, -1],
        [1, -1, 1],
        [-1, -1, 1],
        [-1, -1, -1],
        [0, 1, 0]
    ]

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

    def __init__(self, scale = 1):
        self.edges = Pyramid.edges
        self.vertices = list(numpy.multiply(numpy.array(Pyramid.vertices), scale))

    def draw(self):
        glLineWidth(5)
        glBegin(GL_LINES)
        for edge in self.edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
                glColor3f(0, 0, 1)
        glEnd()

    def move(self, x, y, z):
        self.vertices = list(map(lambda  vertex: (vertex[0] + x, vertex[1] + y, vertex[2] + z), self.vertices))


def main():
    pygame.init()
    display = (screen_height, screen_width)
    # set pygame up for 3d graphics
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0]/display[1]), 0.1, 50)

    # moves back along z direction
    glTranslatef(0, 0, -20)

    p = Pyramid(2)

    velocity = 0.1

    clock = pygame.time.Clock()
    while True:
        clock.tick(60)
        # continually rotate pyramid
        glRotatef(velocity * 10, 0, 1, 0)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            p.move(-velocity, 0, 0)
        if keys[pygame.K_RIGHT]:
            p.move(velocity, 0, 0)
        if keys[pygame.K_UP]:
            p.move(0, velocity, 0)
        if keys[pygame.K_DOWN]:
            p.move(0, -velocity, 0)
        if keys[pygame.K_w]:
            p.move(0, 0, velocity)
        if keys[pygame.K_s]:
            p.move(0, 0, -velocity)
        if keys[pygame.K_a]:
            glRotatef(-velocity*10, 0, 1, 0)
        if keys[pygame.K_d]:
            glRotatef(velocity*10, 0, 1, 0)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        p.draw()
        pygame.display.flip()


main()
