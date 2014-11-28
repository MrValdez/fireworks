import pygame
import random
import math

resolution = [640, 480]
fullscreen = False

pygame.init()

if fullscreen:
    screen = pygame.display.set_mode(resolution, pygame.FULLSCREEN)
else:
    screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

class Launch:
    def __init__(self):
        self.pos = [int(640 / 2), resolution[1] - 1]
        self.life = 300
    
    def update(self, callback_func):
        self.color = pygame.Color(random.randint(0, 255), 
                                  random.randint(0, 255), 
                                  random.randint(0, 255))
        self.pos[1] -= 1
        if random.randint(0, 1) == 0:
            self.pos[0] -= 1
        else:
            self.pos[0] += 1     
        
        self.life -= 1
        
        if self.life <= 0:
            callback_func(self.pos)
    
    def draw(self, screen):
        screen.set_at(self.pos, self.color)

class cBoom:
    def __init__(self, pos):
        self.pos = [pos[0], pos[1]]
        self.angle = random.randint(0, 360) #0 - 360

    def update(self):
        self.color = pygame.Color(random.randint(0, 255), 
                                  random.randint(0, 255), 
                                  random.randint(0, 255))
        self.delta = [random.randint(1,20)*math.cos(math.radians(self.angle)),
                      random.randint(1,20)*math.sin(math.radians(self.angle))]
        
        self.pos[0] += int(self.delta[0])
        self.pos[1] += int(self.delta[1])
    
    def draw(self, screen):
        screen.set_at(self.pos, self.color)
        

GameIsRunning = True
launch = Launch()

ListOfBooms = []

def Boom(pos):
    global launch
    launch = None
    
    for i in range(220):
        ListOfBooms.append(cBoom(pos))

while GameIsRunning:
    #screen.fill([0, 0, 0])

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                GameIsRunning = False
        
        if event.type == pygame.QUIT:
            GameIsRunning = False
        
    if launch: launch.update(Boom)
    
    for boom in ListOfBooms:
        boom.update()
    
    if launch: launch.draw(screen)
    for boom in ListOfBooms:
        boom.draw(screen)
        
    clock.tick(60)
    pygame.display.flip()
    
