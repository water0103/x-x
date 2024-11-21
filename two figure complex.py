import math
import pygame

# 初始化 Pygame
pygame.init()

# 視窗大小及基本設定
window_size = 800
window = pygame.display.set_mode((window_size, window_size))
clock = pygame.time.Clock()
number_of_x = -25

# 定義顏色
white = (255, 255, 255)
green = (0, 255, 0)
blue = (0, 191, 255)
Plum = (221 , 160 , 221)
lavender = (230, 230, 250)
yellow = (255, 255, 0)
red = (255, 0, 0)
DeepPink = (255 , 20 , 147)

# 字體設定
font = pygame.font.Font(None, 36)
title_font = pygame.font.Font(None, 50)

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

# 設置按鈕的屬性
button_rect = pygame.Rect(550, 600, 80, 40)

# 畫面狀態
screen_state = "2d"
x_value_2 = -5
# 主程式迴圈
running = True
l0, l1, l2 = [], [], []
m0, m1, m2 = [], [], []
while running:
    clock.tick(60)
    window.fill((0, 0, 0))

    if screen_state == "2d":
        # 繪製坐標軸
        draw_axes()

        # 繪製 k = 0、k = 1 和 k = 2 的點和連接線
        calculate_and_draw_points(number_of_x, 0, white, l0)
        calculate_and_draw_points(number_of_x, 1, green, l1)
        calculate_and_draw_points(number_of_x, 2, blue, l2)

        # 繪製紅色圓形邊界（模值的範圍）
        pygame.draw.circle(window, red, (window_size // 2, window_size // 2), 100, 2)

        # 顯示文字
        text_x_axis = font.render("Re", True, lavender)
        text_y_axis = font.render("Im", True, lavender)
        text_x = font.render(f'x = {number_of_x:.2f}', True, green)
        text_title = title_font.render("(-1) ** x graph in 2d", True, yellow)
        text_white = font.render("k = 0 : white line", True, white)
        text_green = font.render("k = 1 : green line", True, green)
        text_blue = font.render("k = 2 : blue line", True, blue)

        # 顯示文字到視窗上
        window.blit(text_x_axis, (window_size - 50, window_size / 2))
        window.blit(text_y_axis, (window_size / 2 + 5, 0))
        window.blit(text_x, (150, 600))
        window.blit(text_title, (450, 175))
        window.blit(text_white, (window_size / 8, 125))
        window.blit(text_green, (window_size / 8, 150))
        window.blit(text_blue, (window_size / 8, 175))

        # 繪製按鈕
        pygame.draw.rect(window , blue , button_rect)

        # 渲染按鈕文字
        font = pygame.font.Font(None, 36)
        text_surface = font.render("2d_2", True, white)
        window.blit(text_surface, (button_rect.x + 10, button_rect.y + 10))

        # 更新 x 值
        number_of_x += 0.005
        if number_of_x > 25:
            break

        # 檢查事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    screen_state = "2d_2"

    elif screen_state == "2d_2":
        # 繪製按鈕
        pygame.draw.rect(window , blue , button_rect)

        # 渲染按鈕文字
        font = pygame.font.Font(None, 36)
        text_surface = font.render("2d", True, white)
        window.blit(text_surface, (button_rect.x + 10, button_rect.y + 10))
        
        # 繪製坐標軸
        draw_axes()

        # k = 0
        real_x0, imagine_y0 = real_imagine_root(x_value_2, 0)
        x0 = x_value_2
        x0 = x0 * 10 + window_size / 2
        imagine_y0 = imagine_y0 * 100 + window_size / 2
        points_2d2 = (x0, imagine_y0)  # 將 points_2d2 定義為單一點 (x, y)
        m0.append(points_2d2)  # 將這個點添加到 m0 列表
        connect_points(points_2d2, white)

        # k = 1
        real_x1, imagine_y1 = real_imagine_root(x_value_2, 1)
        x1 = x_value_2
        x1 = x1 * 60 + window_size / 2
        imagine_y1 = imagine_y1 * 100 + window_size / 2
        points_2d2_1 = (x1, imagine_y1)  # 將 points_2d2_1 定義為單一點 (x, y)
        m1.append(points_2d2_1)  # 將這個點添加到 m1 列表
        connect_points(points_2d2_1, green)

        # k = 2
        real_x2, imagine_y2 = real_imagine_root(x_value_2, 2)
        x2 = x_value_2
        x2 = x2 * 60 + window_size / 2
        imagine_y2 = imagine_y2 * 100 + window_size / 2
        points_2d2_2 = (x2, imagine_y2)  # 將 points_2d2_1 定義為單一點 (x, y)
        m2.append(points_2d2_2)  # 將這個點添加到 m1 列表
        connect_points(points_2d2_2, DeepPink)

        # 繪製所有在 m0 列表中的點
        #for point in m0:
            #pygame.draw.circle(window, white, (int(point[0]), int(point[1])), 2)
        #tuple problem(I type that)
        #for i in range(2 , len(m0) - 2 , 2):
            #pygame.draw.line(window , white , (int(m0[i]) , int(m0[i + 1])) , (int(m0[i - 2]) , int(m0[i - 1])) , 2)
        
        for i in range(1, len(m0)):#gpt type these
            pygame.draw.line(window, white, (int(m0[i - 1][0]), int(m0[i - 1][1])), (int(m0[i][0]), int(m0[i][1])), 3)
        for i in range(1, len(m1)):
            pygame.draw.line(window, green, (int(m1[i - 1][0]), int(m1[i - 1][1])), (int(m1[i][0]), int(m1[i][1])), 1)
        for i in range(1, len(m2)):
            pygame.draw.line(window, DeepPink, (int(m2[i - 1][0]), int(m2[i - 1][1])), (int(m2[i][0]), int(m2[i][1])), 1)
        
        x_value_2 += 0.01

        if x_value_2 > 25:
            break
        # 檢查返回主視窗事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    screen_state = "2d"
    pygame.display.flip()

# 結束 Pygame
pygame.quit()