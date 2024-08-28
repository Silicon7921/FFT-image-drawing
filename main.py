import pygame, math, os, sys
from pygame.locals import *

WINDOW_W = 1500
WINDOW_H = 1000
one_time = 1  # time speed (1 by default)
scale = 0.75  # scale
FPS = 144  # framerate (controls game speed) 
point_size = 1
start_xy = (WINDOW_W // 2+500, WINDOW_H // 2+300)  # offset for everything.

b_scale = 1
b_color = (250, 220, 70) # circle color
b_length = 16384

from fourier import PP

fourier_list = PP[:]

# initialize pygame
pygame.init()
pygame.mixer.init()
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (10, 70)
# show window
screen = pygame.display.set_mode((WINDOW_W, WINDOW_H), pygame.DOUBLEBUF, 32)
pygame.display.set_caption("GUI")
font = pygame.font.SysFont('simhei', 20)


class Circle():
    x, y = 0, 0
    r = 0
    angle = 0
    angle_v = 0
    color = (0, 0, 0)
    father = None

    def __init__(self, r, angle_v, angle, color=None, father=None):
        self.r = r
        self.angle_v = angle_v
        self.angle = angle
        self.father = father
        if color is None:
            self.color = (250, 250, 250)
        else:
            self.color = color

    def set_xy(self, xy):
        self.x, self.y = xy

    def get_xy(self):
        return self.x, self.y

    def set_xy_by_angle(self):
        self.x = self.father.x + self.r * math.cos(self.angle) * scale
        self.y = self.father.y + self.r * math.sin(self.angle) * scale

    def run(self, step_time):
        if self.father is not None:
            self.angle += self.angle_v * step_time
            self.set_xy_by_angle()

    def draw(self, screen):
        color_an = tuple(map(lambda x: x // 3, self.color))
        # draw circle
        # print(color_an, int(round(self.x)), self.y)
        pygame.draw.circle(screen, self.color, (int(round(self.x)), int(round(self.y))), point_size)
        if self.father is not None:
            # print(color_an, self.father.x, self.father.y)
            pygame.draw.circle(screen, color_an, (int(round(self.father.x)), int(round(self.father.y))),max(int(round(abs(self.r) * scale)), 1),1)
            pygame.draw.line(screen, self.color, (self.father.x, self.father.y), (self.x, self.y),1)

class Boxin():
    xys = []

    def add_point(self, xy):
        self.xys.append(xy)
        if len(self.xys) > b_length:
            self.xys.pop(0)

    def draw(self, screen):
        bl = len(self.xys)
        for i in range(bl - 1):
            pygame.draw.line(screen, (0, 115, 250), self.xys[i], self.xys[i + 1], 2) #draw track. edit picture color here.


# fourier_list = sorted(fourier_list, key=lambda x: abs(x[0]), reverse=True)
super_circle = Circle(0, 0, 0, color=b_color)
super_circle.set_xy(start_xy)
circle_list = [super_circle]
for i in range(len(fourier_list)):
    p = fourier_list[i]
    circle_list.append(Circle(p[0], p[1], p[2], color=b_color, father=circle_list[i]))

bx = Boxin()
clock = pygame.time.Clock()

# game main cycle
while True:
    
    # handle exit operation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # background
    screen.fill((20, 22, 25))
    # run
    for i, circle in enumerate(circle_list):
        circle.run(1)
        circle.draw(screen)

    last_circle = circle_list[-1]
    bx.add_point((last_circle.x, last_circle.y))
    bx.draw(screen)

    pygame.display.update()
    time_passed = clock.tick(FPS)
