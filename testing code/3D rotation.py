import pygame
import math
import numpy as np

# Pygame 初始化
window_size = 800
window = pygame.display.set_mode((window_size, window_size))
pygame.display.set_caption("3D Graph Projection")
clock = pygame.time.Clock()

# 顏色
white = (255, 255, 255)
blue = (0, 191, 255)
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

# 旋轉矩陣
def rotate_3d(point, angle_x, angle_y, angle_z):
    x, y, z = point[0], point[1], point[2]
    # X 軸旋轉
    y, z = (y * math.cos(angle_x) - z * math.sin(angle_x),
            y * math.sin(angle_x) + z * math.cos(angle_x))
    # Y 軸旋轉
    x, z = (x * math.cos(angle_y) + z * math.sin(angle_y),
            -x * math.sin(angle_y) + z * math.cos(angle_y))
    # Z 軸旋轉
    x, y = (x * math.cos(angle_z) - y * math.sin(angle_z),
            x * math.sin(angle_z) + y * math.cos(angle_z))
    return (x, y, z)

# 初始化參數
points_3d = []
x_start, x_end = -5, 5
x_step = 0.1
k = 0  # 固定 k 值
angle_x = angle_y = angle_z = 0
fov = 200  # 視角大小
distance = 5  # 透視距離

# 生成 3D 點
x_value = x_start
while x_value <= x_end:
    real, x, imagine = function(x_value, k)
    points_3d.append((real * 100, x * 100, imagine * 100))
    x_value += x_step

# 主迴圈
running = True
while running:
    clock.tick(60)
    window.fill(black)

    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新旋轉角度
    angle_x += 0.01
    angle_y += 0.01
    angle_z += 0.01

    # 投影並繪製點
    projected_points = []
    for point in points_3d:
        rotated_point = rotate_3d(point, angle_x, angle_y, angle_z)
        projected_point = project_3d_to_2d(rotated_point, fov, distance)
        projected_points.append(projected_point)

    # 繪製點之間的連線
    for i in range(1, len(projected_points)):
        pygame.draw.line(window, blue, projected_points[i - 1], projected_points[i], 2)

    pygame.display.flip()

pygame.quit()
