# e ^ i * (2 * k * pi + pi) * x
import math
import pygame
import numpy as np

pygame.init()

window_size = 800

window = pygame.display.set_mode((window_size , window_size))
time = pygame.time.Clock()

x_changing = -5
l0 = []
l1 = []
l2 = []

white = (255, 255 ,255)
green = (0, 255, 0)
DeepPink = (255, 20, 147)

def factor(x):
    return x * 100 + window_size / 2

def function(x , k):
    # func = math.exp(2 * k * math.pi + math.pi) * x * 1j
    basic_number = (2 * k * math.pi + math.pi) * x
    real_number = math.cos(basic_number)
    imagine_number = math.sin(basic_number)
    x0 = x
    #return factor(x0) , factor(real_number) , factor(imagine_number)
    return x0 , real_number , imagine_number

def pro_matrix(x , y , z , fov = math.radians(math.pi / 4)):
    x_proj = x + y * math.pow(math.cos(fov) , 2)
    y_proj = z + y * math.pow(math.cos(fov) , 2)
    return factor(x_proj) , factor(y_proj)

running = True
times = 0
while(running):
    time.tick(60)
    window.fill((0,0,0))
    # k = 0
    x0 , real0 , imagine0 = function(x_changing , 0)
    projection_x , projection_y = pro_matrix(x0 , real0 , imagine0)
    l0.append((projection_x , projection_y))

    # k = 1
    x1 , real1 , imagine1 = function(x_changing , 1)
    projection_x , projection_y = pro_matrix(x1 , real1 , imagine1)
    l1.append((projection_x , projection_y))
    
    # k = 2
    x2 , real2 , imagine2 = function(x_changing , 2)
    projection_x , projection_y = pro_matrix(x2 , real2 , imagine2)
    l2.append((projection_x , projection_y))

    for i in range(1 , len(l0)):
        pygame.draw.line(window, white , (int(l0[i-1][0]) , int(l0[i-1][1])) , (int(l0[i][0]) , int(l0[i][1])) , 2)
    for i in range(1 , len(l1)):
        pygame.draw.line(window, green , (int(l1[i-1][0]) , int(l1[i-1][1])) , (int(l1[i][0]) , int(l1[i][1])) , 1)
    for i in range(1 , len(l2)):
        pygame.draw.line(window, DeepPink , (int(l2[i-1][0]) , int(l2[i-1][1])) , (int(l2[i][0]) , int(l2[i][1])) , 1)

    x_changing += 0.015
    times += 1
    if times >= 1000:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()