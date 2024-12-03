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

number_of_x = -10
l = []
running = True
projection_matrix = np.matrix([[1,0,0],
                               [0,1,0],
                               [0,0,0]])

angle_x = angle_y = angle_z = 0

while(running):
    three_d_points = np.matrix([[0],[0],[0]])
    time.tick(60)
    window.fill((0 , 0 , 0))

    # rotation objects
    rotation_x = [[1 , 0 , 0],
                  [0 , math.cos(angle_x) , -math.sin(angle_x)],
                  [0 , math.sin(angle_x) , math.cos(angle_x)]]
    rotation_y = [[math.cos(angle_y) , 0 , math.sin(angle_y)],
                  [0 , 1 , 0],
                  [-math.sin(angle_y) , 0 , math.cos(angle_y)]]
    rotation_z = [[math.cos(angle_z) , -math.sin(angle_z) , 0],
                  [math.sin(angle_z) , math.cos(angle_z) , 0],
                  [0 , 0 , 1]]
    
    angle_x += 0.001
    angle_y += 0.001
    angle_z += 0.001 

    #標點 存放在l array
    real_x , x_y , imagine_z = function(number_of_x , 0)
    real_x = real_x * 100 + windowsize / 2
    x_y = x_y * 100 + windowsize / 2
    imagine_z = imagine_z * 100 + windowsize / 2
    three_d_points[0][0] = x_y
    three_d_points[1][0] = imagine_z
    three_d_points[2][0] = real_x
    rotatex = np.dot(rotation_x , three_d_points)
    rotatey = np.dot(rotation_y , three_d_points)
    rotatez = np.dot(rotation_z , three_d_points)
    points = np.dot(projection_matrix , rotatez)
    x = points[0][0]
    y = points[1][0]
    l.append((x , y))

    for i in range(1 , len(l)):
        pygame.draw.line(window , white , (int(l[i-1][0]) , int(l[i-1][1])) , (int(l[i][0]) , int(l[i][1])) , 1)

    number_of_x += 0.05
    if number_of_x > 10:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit