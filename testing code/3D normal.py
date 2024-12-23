import pygame
import math
import numpy as np

# 初始化 Pygame
window_size = 800
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("3D Graph with Axes")
clock = pygame.time.Clock()

# 顏色
white = (255, 255, 255)
blue = (0, 191, 255)
red = (255, 0, 0)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)

# 定義函數
def function(x, k):
    real = math.cos((2 * k + 1) * math.pi * x)  # 實部
    imagine = math.sin((2 * k + 1) * math.pi * x)  # 虛部
    return real, x, imagine

# 3D 到 2D 投影矩陣 (透視投影)
def project_3d_to_2d(point, fov, distance):
    x, y, z = point[0], point[1], point[2]
    if z != 0:
        factor = fov / (distance + z)
        x = x * factor + window_size / 2
        y = -y * factor + window_size / 2
    return (int(x), int(y))

# 初始化參數
points_3d = []
x_start, x_end = -5, 5
x_step = 0.1
k = 0  # 固定 k 值
fov = 200  # 視角大小
distance = 5  # 透視距離

# 生成 3D 點
x_value = x_start
while x_value <= x_end:
    real, x, imagine = function(x_value, k)
    points_3d.append((real * 100, x * 100, imagine * 100))
    x_value += x_step

# 定義座標軸的3D點
axis_points_3d = [
    # X 軸
    (-150, 0, 0), (150, 0, 0),
    # Y 軸
    (0, -150, 0), (0, 150, 0),
    # Z 軸
    (0, 0, -150), (0, 0, 150)
]

# 主迴圈
running = True
while running:
    clock.tick(60)
    window.fill(black)

    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 繪製座標軸
    projected_axis_points = []
    for point in axis_points_3d:
        projected_axis_points.append(project_3d_to_2d(point, fov, distance))
    
    # 繪製 X 軸
    pygame.draw.line(window, red, projected_axis_points[0], projected_axis_points[1], 2)
    # 繪製 Y 軸
    pygame.draw.line(window, green, projected_axis_points[2], projected_axis_points[3], 2)
    # 繪製 Z 軸
    pygame.draw.line(window, yellow, projected_axis_points[4], projected_axis_points[5], 2)

    # 投影並繪製函數點
    projected_points = []
    for point in points_3d:
        projected_point = project_3d_to_2d(point, fov, distance)
        projected_points.append(projected_point)

    # 繪製點之間的連線
    for i in range(1, len(projected_points)):
        pygame.draw.line(window, blue, projected_points[i - 1], projected_points[i], 2)

    pygame.display.flip()

pygame.quit()
