import pygame
import math
import numpy as np

windowsize = 800
window = pygame.display.set_mode((windowsize , windowsize))
time = pygame.time.Clock()

#color
white = (255 , 255 , 255)

def function(x , k):
    real = math.cos((2 * k + 1) * math.pi * x)
    imagine = math.sin((2 * k + 1) * math.pi * x)
    x0 = x
    return real , x0 , imagine

number_of_x = -5
l = []
running = True
projection_matrix = np.matrix([[1,0,0],
                               [0,1,0],
                               [0,0,0]])

while(running):
    three_d_points = [[0],[0],[0]]
    time.tick(60)
    window.fill((0 , 0 , 0))

    #標點 存放在l array
    real_x , x_y , imagine_z = function(number_of_x , 0)
    real_x = real_x * 100 + windowsize / 2
    x_y = x_y * 100 + windowsize / 2
    imagine_z = imagine_z * 100 + windowsize / 2
    three_d_points[0][0] = x_y
    three_d_points[1][0] = imagine_z
    three_d_points[2][0] = real_x
    points = np.dot(projection_matrix , three_d_points)
    x = points[0][0]
    y = points[1][0]
    l.append((x , y))

    for i in range(1 , len(l)):
        pygame.draw.line(window , white , (int(l[i-1][0]) , int(l[i-1][1])) , (int(l[i][0]) , int(l[i][1])) , 1)

    number_of_x += 0.02
    if number_of_x > 5:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit