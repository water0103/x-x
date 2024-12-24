import math
import numpy as np
import pygame

# 初始化 Pygame
pygame.init()

# 視窗大小及基本設定
window_size = 800
window = pygame.display.set_mode((window_size , window_size))
clock = pygame.time.Clock()

# 定義顏色
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 191, 255)
Plum = (221, 160, 221)
lavender = (230, 230, 250)
yellow = (255, 255, 0)
red = (255, 0, 0)
DeepPink = (255, 20, 147)

# 字體設定
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 50)

# 倍率設定
def factor(x):
    return x * 100 + window_size / 2

# 實部，虛部，x值
def function(x , k):
    basic_number = (2 * k * math.pi + math.pi) * x
    real_number = math.cos(basic_number)
    imagine_number = math.sin(basic_number)
    x0 = x
    return x0 , real_number , imagine_number

# 斜投影矩陣
def pro_matrix(x , y , z , fov = math.radians(math.pi / 4)):
    x_proj = x + y * math.pow(math.cos(fov) , 2)
    y_proj = z + y * math.pow(math.cos(fov) , 2)
    return factor(x_proj) , factor(y_proj)

# 計算實部與虛部的函數
def real_imagine_root(x, k):
    real = math.cos((2 * k + 1) * math.pi * x)
    imagine = math.sin((2 * k + 1) * math.pi * x)
    return real, imagine

# 繪製線條的函數
def connect_points(points, color):
    pygame.draw.line(window, color, (points[0], points[1]), (window_size / 2, window_size / 2), 5)

# 封裝繪製點和連接線的函數
def calculate_and_draw_points(x_value, k, color, points_list):
    real_x, imagine_y = real_imagine_root(x_value, k)
    real_x = real_x * 100 + window_size / 2
    imagine_y = imagine_y * 100 + window_size / 2
    points = [real_x, imagine_y]
    points_list.append((real_x, imagine_y))
    connect_points(points, color)

# 繪製坐標軸的函數
def draw_axes():
    pygame.draw.line(window, Plum, (0, window_size / 2), (window_size, window_size / 2), 2)
    pygame.draw.line(window, Plum, (window_size / 2, 0), (window_size / 2, window_size), 2)

# 繪製按鈕的函數
def draw_button(label, color, rect):
    pygame.draw.rect(window, color, rect)
    text_surface = font.render(label, True, white)
    window.blit(text_surface, (rect.x + 15, rect.y + 10))

# xxfuntion
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

# 設置按鈕的屬性
button_rect = pygame.Rect(550, 600, 120, 40)

# 畫面狀態和變數初始化
screen_state = "2d"
number_of_x = -5
x_value_2 = -5
x_changing = -5
x_changing2 = -5
l0, l1, l2 = [], [], []
m0, m1, m2 = [], [], []
n0, n1, n2 = [], [], []
o0, o1, o2 = [], [], []
o4 = []
running = True
times = 0
times2 = 0

# 主程式迴圈
while running:
    clock.tick(60)
    window.fill((0, 0, 0))

    if screen_state == "2d":
        draw_axes()
        calculate_and_draw_points(number_of_x, 0, white, l0)
        calculate_and_draw_points(number_of_x, 1, green, l1)
        calculate_and_draw_points(number_of_x, 2, blue, l2)
        pygame.draw.circle(window, red, (window_size // 2, window_size // 2), 100, 5)
        text_x_axis = font.render("Re", True, lavender)
        text_y_axis = font.render("Im", True, lavender)
        text_x = font.render(f'x = {number_of_x:.2f}', True, green)
        text_title = title_font.render("(-1) ** x graph in 2d", True, yellow)
        text_white = font.render("k = 0 : white line", True, white)
        text_green = font.render("k = 1 : green line", True, green)
        text_blue = font.render("k = 2 : blue line", True, blue)

        window.blit(text_x_axis, (window_size - 50, window_size / 2))
        window.blit(text_y_axis, (window_size / 2 + 5, 0))
        window.blit(text_x, (150, 600))
        window.blit(text_title, (450, 175))
        window.blit(text_white, (window_size / 8, 125))
        window.blit(text_green, (window_size / 8, 150))
        window.blit(text_blue, (window_size / 8, 175))
        draw_button("2d_2", blue, button_rect)

        number_of_x += 0.005
        if number_of_x > 5:
            running = False

        # 檢查事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                screen_state = "2d_2"

    elif screen_state == "2d_2":
        draw_axes()
        draw_button("3d_1", blue, button_rect)

        # 繪製 k = 0、k = 1、k = 2 的點和連接線
        for k, color, scale, points_list in [(0, white, 10, m0), (1, green, 60, m1), (2, DeepPink, 60, m2)]:
            real_x, imagine_y = real_imagine_root(x_value_2, k)
            x = x_value_2 * scale + window_size / 2
            y = imagine_y * 100 + window_size / 2
            point = (x, y)
            points_list.append(point)
            connect_points(point, color)

        # 繪製列表中的點
        for points_list, color, width in [(m0, white, 3), (m1, green, 2), (m2, DeepPink, 1)]:
            for i in range(1, len(points_list)):
                pygame.draw.line(window, color, (int(points_list[i - 1][0]), int(points_list[i - 1][1])),
                                 (int(points_list[i][0]), int(points_list[i][1])), width)
                
        
        text_x_axis = font.render("X", True, lavender)
        text_y_axis = font.render("Im", True, lavender)
        text_x = font.render(f'x = {x_value_2:.2f}', True, green)
        text_title = title_font.render("(-1) ** x graph in 2d", True, yellow)
        text_white = font.render("k = 0 : white line", True, white)
        text_green = font.render("k = 1 : green line", True, green)
        text_deeppink = font.render("k = 2 : DeepPink line", True, DeepPink)

        window.blit(text_x_axis, (window_size - 45, window_size / 2))
        window.blit(text_y_axis, (window_size / 2 + 5, 0))
        window.blit(text_x, (150, 600))
        window.blit(text_title, (450, 175))
        window.blit(text_white, (window_size / 8, 125))
        window.blit(text_green, (window_size / 8, 150))
        window.blit(text_deeppink, (window_size / 8, 175))

        x_value_2 += 0.005
        if x_value_2 > 5:
            running = False

        # 檢查事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                screen_state = "3d"

    elif screen_state == "3d":
        draw_button("x ** x  3d", blue, button_rect)

        # k = 0
        x0 , real0 , imagine0 = function(x_changing , 0)
        projection_x , projection_y = pro_matrix(x0 , real0 , imagine0)
        n0.append((projection_x , projection_y))

        # k = 1
        x1 , real1 , imagine1 = function(x_changing , 1)
        projection_x , projection_y = pro_matrix(x1 , real1 , imagine1)
        n1.append((projection_x , projection_y))

        # k = 2
        x2 , real2 , imagine2 = function(x_changing , 2)
        projection_x , projection_y = pro_matrix(x2 , real2 , imagine2)
        n2.append((projection_x , projection_y))

        for i in range(1 , len(n0)):
            pygame.draw.line(window, white , (int(n0[i-1][0]) , int(n0[i-1][1])) , (int(n0[i][0]) , int(n0[i][1])) , 2)
        for i in range(1 , len(n1)):
            pygame.draw.line(window, green , (int(n1[i-1][0]) , int(n1[i-1][1])) , (int(n1[i][0]) , int(n1[i][1])) , 1)
        for i in range(1 , len(n2)):
            pygame.draw.line(window, DeepPink , (int(n2[i-1][0]) , int(n2[i-1][1])) , (int(n2[i][0]) , int(n2[i][1])) , 1)
        
        text_x = font.render(f'x = {x_changing:.2f}', True, green)
        text_title = title_font.render("(-1) ** x graph in 3d", True, yellow)
        text_white = font.render("k = 0 : white line", True, white)
        text_green = font.render("k = 1 : green line", True, green)
        text_deeppink = font.render("k = 2 : DeepPink line", True, DeepPink)

        window.blit(text_x, (150, 600))
        window.blit(text_title, (450, 175))
        window.blit(text_white, (window_size / 8, 125))
        window.blit(text_green, (window_size / 8, 150))
        window.blit(text_deeppink, (window_size / 8, 175))

        x_changing += 0.015
        times += 1

        if times >= 1000:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                screen_state = "xx3d"
    elif screen_state == "xx3d":
        draw_button("(-1) ** x 2d" , blue , button_rect)

        xx0 , xreal0 , ximagine0 = com_function(x_changing2 , 3)
        projection_x , projection_y = pro_matrix(xx0 , xreal0 , ximagine0)
        o0.append((projection_x , projection_y))

        xx1 , xreal1 , ximagine1 = com_function(x_changing2 , 1)
        projection_x , projection_y = pro_matrix(xx1 , xreal1 , ximagine1)
        o1.append((projection_x , projection_y))

        xx2 , xreal2 , ximagine2 = com_function(x_changing2 , 2)
        projection_x , projection_y = pro_matrix(xx2 , xreal2 , ximagine2)
        o2.append((projection_x , projection_y))

        xx4 , xreal4 , ximagine4 = com_function(x_changing2 , 4)
        projection_x , projection_y = pro_matrix(xx4 , xreal4 , ximagine4)
        o4.append((projection_x , projection_y))

        for i in range(1 , len(o0)):
            pygame.draw.line(window , white , (int(o0[i-1][0]) , int(o0[i-1][1])) , (int(o0[i][0]) , int(o0[i][1])) , 2)
        for i in range(1 , len(o1)):
            pygame.draw.line(window , green , (int(o1[i-1][0]) , int(o1[i-1][1])) , (int(o1[i][0]) , int(o1[i][1])) , 1)
        for i in range(1 , len(o2)):
            pygame.draw.line(window , DeepPink , (int(o2[i-1][0]) , int(o2[i-1][1])) , (int(o2[i][0]) , int(o2[i][1])) , 1)
        for i in range(1 , len(o4)):
            pygame.draw.line(window , blue , (int(o4[i-1][0]) , int(o4[i-1][1])) , (int(o4[i][0]) , int(o4[i][1])) , 1)
        
        text_x = font.render(f'x = {x_changing2:.2f}', True, green)
        text_title = title_font.render("x ** x graph in 3d", True, yellow)
        text_white = font.render("k = 3 : white line", True, white)
        text_green = font.render("k = 1 : green line", True, green)
        text_deeppink = font.render("k = 2 : DeepPink line", True, DeepPink)
        text_blue = font.render("k = 4 : blue line" , True , blue)

        window.blit(text_x, (150, 600))
        window.blit(text_title, (450, 175))
        window.blit(text_white, (window_size / 8, 175))
        window.blit(text_green, (window_size / 8, 125))
        window.blit(text_deeppink, (window_size / 8, 150))
        window.blit(text_blue, (window_size / 8 , 200))

        x_changing2 += 0.01
        times2 += 1
        
        if times2 >= 100000:
            running = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                screen_state = "2d"
    pygame.display.flip()
    
# 結束 Pygame
pygame.quit()