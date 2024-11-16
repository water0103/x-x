#y = (-1) ** x = math.exp((2 * k * math.pi + math.pi) * x * 1j)
import math
import numpy as np
import pygame
#x with using while
#k with using for i in range

window_size = 800
window = pygame.display.set_mode((window_size , window_size))
time = pygame.time.Clock()
number_of_x = -25
points = []

def real_imagine_root(x):
    real = math.cos(math.pi * x)
    imagine = math.sin(math.pi * x)
    return real , imagine

while(number_of_x < 25):
    time.tick(60)
    window.fill((0 , 0 , 0))
    real_x , imagine_y = real_imagine_root(number_of_x)
    real_x = real_x * 100 + window_size / 2
    imagine_y = imagine_y * 100 + window_size / 2
    points.append((real_x , imagine_y))
    for point in points:
        pygame.draw.circle(window , (255 , 0 , 0) , (round(point[0]) , round(point[1])) , 5)
    number_of_x += 0.01
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update