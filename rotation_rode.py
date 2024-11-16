# y = (-1) ** x = math.exp((2 * k * math.pi + math.pi) * x * 1j)
import math
import pygame
# x with using while

# 初始化 Pygame
pygame.init()

window_size = 800
window = pygame.display.set_mode((window_size, window_size))
clock = pygame.time.Clock()
number_of_x = -25
l = l1 = l2 = []

# define color
white = (255 , 255 , 255)
green = (0 , 255 , 0)
blue = (0 , 191 , 255)
violet = (238 , 130 , 238)
lavender = (230 , 230 , 250)
Yellow1 = (255 , 255 , 0)
red = (255 , 0 , 0)

# the parameter of the axes name
# None 使用預設字體，36 是字體大小
font = pygame.font.Font(None, 36)
title = pygame.font.Font(None , 50)

# 計算實部與虛部的函數
def real_imagine_root(x , k):
    real =math.cos((2 * k + 1) * math.pi * x)
    imagine =math.sin((2 * k + 1) * math.pi * x)
    return real, imagine

def connect_points(points , color):
    pygame.draw.line(window , color , (points[0] , points[1]) , (window_size / 2 , window_size / 2) , 5)

# x axes and y axes
def draw_axes():
    pygame.draw.line(window , violet , (0 , window_size / 2) , (window_size , window_size / 2) , 2)
    pygame.draw.line(window , violet , (window_size / 2 , 0) , (window_size / 2 , window_size) , 2)

running = True
while running: 
    points = [0 , 0]
    points1 = [0 , 0]
    points2 = [0 , 0]
    clock.tick(60)
    window.fill((0, 0, 0))

    # 座標軸
    draw_axes()

    # for k = 0
    real_x, imagine_y = real_imagine_root(number_of_x , 0)
    real_x = real_x * 100 + window_size / 2
    imagine_y = imagine_y * 100 + window_size / 2
    points[0] = real_x
    points[1] = imagine_y
    l.append((real_x , imagine_y))

    # for k = 1
    real_x1, imagine_y1 = real_imagine_root(number_of_x , 1)
    real_x1 = real_x1 * 100 + window_size / 2
    imagine_y1 = imagine_y1 * 100 + window_size / 2
    points1[0] = real_x1
    points1[1] = imagine_y1
    l1.append((real_x1 , imagine_y1))

    # for k = 2
    real_x2, imagine_y2 = real_imagine_root(number_of_x , 2)
    real_x2 = real_x2 * 100 + window_size / 2
    imagine_y2 = imagine_y2 * 100 + window_size / 2
    points2[0] = real_x2
    points2[1] = imagine_y2
    l2.append((real_x2 , imagine_y2))

    # 函數的模
    pygame.draw.circle(window , red , (window_size // 2 , window_size // 2) , 100 , 2)
    # 繪製k = 0所有計算的浮點數座標點
    connect_points(points , white)
    # 繪製k = 1所有計算的浮點數座標點
    connect_points(points1 , green)
    # 繪製k = 2所有計算的浮點數座標點
    connect_points(points2 , blue) 

    # 渲染並顯示文字
    text_x_axis = font.render("Re" , True , lavender)
    text_y_axis = font.render("Im" , True , lavender)
    text_x = font.render(f'x = {number_of_x:.2f}' , True , green)
    text_title = title.render("(-1) ** x graph in 2d" , True , Yellow1)
    text_white = font.render("k = 0 : white line" , True , white)
    text_green = font.render("k = 1 : green line" , True , green)
    text_blue = font.render("k = 2 : blue line" , True , blue)
    window.blit(text_x_axis , (window_size - 50 , window_size / 2))
    window.blit(text_y_axis , (window_size / 2 + 5, 0))
    window.blit(text_x , (150 , 600))
    window.blit(text_title , (450 , 175))
    window.blit(text_white , (window_size / 8 , 125))
    window.blit(text_green , (window_size / 8 , 150))
    window.blit(text_blue , (window_size / 8 , 175))

    number_of_x += 0.005
    if number_of_x > 25:
        break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# 退出 Pygame
pygame.quit()