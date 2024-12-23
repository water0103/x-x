# for x > 0: y = abs(x) ** x * math.exp(2 * k * math.pi * x  * 1j)
# for x < 0: y = abs(x) ** x * math.exp((2 * k * math.pi + math.pi) * x * 1j)
import math
import pygame

pygame.init()

window_size = 800

window = pygame.display.set_mode((window_size , window_size))
time = pygame.time.Clock()

x_changing = -5
o0, o1 , o2 = [] , [] , []

white = (255, 255, 255)
green = (0, 255, 0)
DeepPink = (255, 20, 147)

def factor(x):
    return x * 100 + window_size / 2

def com_function(x , k):
    ro = abs(x)
    if x > 0:
        basic_number = (2 * k * math.pi) * x
    if x < 0:
        basic_number = (2 * k * math.pi + math.pi) * x
    if x == 0:
        basic_number = 0
    real_number = math.cos(basic_number) * ro ** x
    imagine_number = math.sin(basic_number) * ro ** x
    x0 = x
    return x0 , real_number , imagine_number

def pro_matrix(x , y , z , fov = math.radians(math.pi / 4)):
    x_proj = x + y * math.pow(math.cos(fov) , 2)
    y_proj = z + y * math.pow(math.cos(fov) , 2)
    return factor(x_proj) , factor(y_proj)

running = True
times = 0
while(running):
    time.tick(60)
    window.fill((0, 0, 0))

    x0 , real0 , imagine0 = com_function(x_changing , 3)
    projection_x , projection_y = pro_matrix(x0 , real0 , imagine0)
    o0.append((projection_x , projection_y))

    x1 , real1 , imagine1 = com_function(x_changing , 1)
    projection_x , projection_y = pro_matrix(x1 , real1 , imagine1)
    o1.append((projection_x , projection_y))

    x2 , real2 , imagine2 = com_function(x_changing , 2)
    projection_x , projection_y = pro_matrix(x2 , real2 , imagine2)
    o2.append((projection_x , projection_y))

    for i in range(1 , len(o0)):
       pygame.draw.line(window , white , (int(o0[i-1][0]) , int(o0[i-1][1])) , (int(o0[i][0]) , int(o0[i][1])) , 2)
    for i in range(1 , len(o1)):
       pygame.draw.line(window , green , (int(o1[i-1][0]) , int(o1[i-1][1])) , (int(o1[i][0]) , int(o1[i][1])) , 1)
    for i in range(1 , len(o2)):
       pygame.draw.line(window , DeepPink , (int(o2[i-1][0]) , int(o2[i-1][1])) , (int(o2[i][0]) , int(o2[i][1])) , 1)

    x_changing += 0.012
    times += 1
    if times >= 1000:
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()