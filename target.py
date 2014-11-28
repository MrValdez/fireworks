import pygame
import random
import math

pygame.init()

resolution = [640, 480]
fullscreen = False
if fullscreen:
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

GameIsRunning = True

class tail:
    def __init__(self):
        self.pos = [random.randint(0, 640), random.randint(400, 400)]
        self.life = random.randint(0, 10)

    def update(self, callback_func):
        self.pos[1] -= 1
        if random.randint(0, 1):
            self.pos[0] -= 1
        else:
            self.pos[0] += 1
            
        self.color = pygame.Color(255, 255, 255)
        self.life -= 1
        
        if self.life < 0:
            callback_func(self.pos)

    def draw(self, screen):
        screen.set_at(self.pos, self.color)
        
class Head:
    def __init__(self, pos):
        self.pos = [pos[0], pos[1]]
        self.angle = math.radians(45)

    def update(self):
        self.color = pygame.Color(255, 
                                  random.randint(0, 255),
                                  random.randint(0, 255))
        self.angle = math.radians(random.randint(10,170))
        distance = [2 * math.cos(self.angle),
                   3 * math.sin(self.angle)]

        self.pos[0] += int(distance[0])
        self.pos[1] += int(distance[1])
        
        #self.pos[1] -= 2

    def draw(self, screen):
        screen.set_at(self.pos, self.color)
        
tail = tail()
heads = []

def make_boom(pos):
    global tail, heads
    tail = None
    for i in range(10):
        head = Head(pos)
        heads.append(head)

while GameIsRunning:
    #screen.fill([0, 0, 0])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameIsRunning = False
        
        if event.type == pygame.QUIT:
            GameIsRunning = False

    if tail: tail.update(make_boom)
    for head in heads:
        head.update()
    
    if tail: tail.draw(screen)
    for head in heads:
        head.draw(screen)    

    clock.tick(10)
    pygame.display.flip()
    
