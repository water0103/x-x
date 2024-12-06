import pygame
import math
import numpy as np

windowsize = 1000
window = pygame.display.set_mode((windowsize , windowsize))
time = pygame.time.Clock()

#color
white = (255 , 255 , 255)
Plum = (221 , 160 , 221)

def function(x , k):
    real = math.cos((2 * k + 1) * math.pi * x)
    imagine = math.sin((2 * k + 1) * math.pi * x)
    x0 = x
    return x0 , real , imagine

number_of_x = -5
l1 = l = []
running = True
projection_matrix = np.matrix([[1,0,0],
                               [0,1,0],
                               [0,0,0]])

fov = 200  # 視場角
distance = 5  # 視距

def project_3d_to_2d(point, fov, distance):
    x, y, z = point[0], point[1], point[2]
    if z != 0:
        factor = fov / (distance + z)
        x = x * factor + windowsize / 2
        y = -y * factor + windowsize / 2
    return (int(x), int(y))


while(running):
    time.tick(60)
    window.fill((0 , 0 , 0))
    three_d_points = np.matrix([[0],[0],[0]])
    three_d_points1 = np.matrix([[0],[0],[0]])

    #標點 存放在l array
    x , imagine , real = function(number_of_x , 0)
    x = x * 100 + windowsize / 2
    imagine = imagine * 100 + windowsize / 2
    real = imagine * 100 + windowsize / 2
    three_d_points1[0][0] = x
    three_d_points1[1][0] = imagine
    three_d_points1[2][0] = real
    points1 = project_3d_to_2d(three_d_points1)
    x1 = x
    y1 = imagine
    l1.append((x1 , y1))

    for i in range(1 , len(l1)):
        pygame.draw.line(window , white, (int(l1[i-1][0]) , int(l1[i-1][1])) , (int(l1[i][0]) , int(l1[i][1])) , 1)
    '''
    real_x , x_y , imagine_z = function(number_of_x , 0)
    real_x = real_x * 100 + windowsize / 2
    x_y = x_y * 100 + windowsize / 2
    imagine_z = imagine_z * 100 + windowsize / 2
    three_d_points[0][0] = real_x
    three_d_points[1][0] = imagine_z
    three_d_points[2][0] = real_x
    points = np.dot(projection_matrix , three_d_points)
    x = points[0][0]
    y = points[1][0]
    l.append((x , y))

    for i in range(1 , len(l)):
        pygame.draw.line(window , white , (int(l[i-1][0]) , int(l[i-1][1])) , (int(l[i][0]) , int(l[i][1])) , 1)
    '''
    number_of_x += 0.01
    if number_of_x > 5:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit