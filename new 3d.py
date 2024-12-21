# e ^ i * (2 * k * pi + pi) * x
import math
import pygame
import numpy as np

pygame.init()

window_size = 800
'''
window = pygame.display.set_mode((window_size , window_size))
clock = pygame.time.Clock()
'''
x_changing = -10
l = []

white = (255, 255 ,255)

def factor(x):
    return x * 100 + window_size / 2

def function(x , k):
    # func = math.exp(2 * k * math.pi + math.pi) * x * 1j
    basic_number = (2 * k * math.pi + math.pi) * x
    real_number = math.cos(basic_number)
    imagine_number = math.sin(basic_number)
    x0 = x
    return factor(x0) , factor(real_number) , factor(imagine_number)
    #return x0 , real_number , imagine_number

def build_projection_matrix(fov, aspect, zn, zf):
    # 初始化矩陣
    proj = np.zeros((4, 4), dtype=float)

    # 計算投影矩陣
    proj[0][0] = 1 / (math.tan(fov * 0.5) * aspect)
    proj[1][1] = 1 / math.tan(fov * 0.5)
    proj[2][2] = zf / (zf - zn)
    proj[2][3] = 1.0
    proj[3][2] = (zn * zf) / (zn - zf)

    return proj

running = True
while(running):
    points = np.matrix([0],[0],[0])

    x , real , imagine = function(x_changing , 0)
    points[0][0] = x
    points[1][0] = real
    points[2][0] = imagine
