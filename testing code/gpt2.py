import pygame
import math
import numpy as np

# 初始化 Pygame
windowsize = 1000
window = pygame.display.set_mode((windowsize, windowsize))
time = pygame.time.Clock()

# 顏色設定
white = (255, 255, 255)

# 投影函數：3D -> 2D
def project_3d_to_2d(point, fov, distance):
    x, y, z = point[0], point[1], point[2]
    factor = fov / (distance + z) if distance + z != 0 else 0.001
    x_2d = x * factor + windowsize / 2
    y_2d = -y * factor + windowsize / 2  # 翻轉 y 軸
    return int(x_2d), int(y_2d)

# 定義旋轉矩陣（改變視角）
def rotate_3d(point, angle_x, angle_y):
    # Rotation around the X-axis
    rotation_x = np.array([
        [1, 0, 0],
        [0, math.cos(angle_x), -math.sin(angle_x)],
        [0, math.sin(angle_x), math.cos(angle_x)]
    ])
    # Rotation around the Y-axis
    rotation_y = np.array([
        [math.cos(angle_y), 0, math.sin(angle_y)],
        [0, 1, 0],
        [-math.sin(angle_y), 0, math.cos(angle_y)]
    ])
    # Apply rotations
    rotated_point = np.dot(rotation_y, np.dot(rotation_x, point))
    return rotated_point

# 主程式變數
running = True
fov = 500  # 視場角
distance = 200  # 視距
l = []  # 用於儲存三維點
angle_step = 0.1  # 每次增加的角度步進
z_step = 2  # 每次沿 z 軸的位移步進
radius = 200  # 螺旋半徑
angle = 0  # 初始角度
z = -500  # 初始 z 軸位置
view_angle_x = math.radians(30)  # 沿 X 軸的視角旋轉
view_angle_y = math.radians(30)  # 沿 Y 軸的視角旋轉

# 主迴圈
while running:
    time.tick(60)
    window.fill((0, 0, 0))

    # 計算新 3D 點並存入列表
    x = radius * math.cos(angle)
    y = radius * math.sin(angle)
    point_3d = np.array([x, y, z])

    # 應用旋轉矩陣
    rotated_point = rotate_3d(point_3d, view_angle_x, view_angle_y)
    l.append(rotated_point)

    # 更新參數
    angle += angle_step  # 增加角度
    z += z_step  # 增加 z 軸位移

    # 繪製螺旋
    if len(l) > 1:
        for i in range(1, len(l)):
            p1 = project_3d_to_2d(l[i - 1], fov, distance)
            p2 = project_3d_to_2d(l[i], fov, distance)
            pygame.draw.line(window, white, p1, p2, 1)

    # 處理事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 更新畫面
    pygame.display.flip()

    # 停止條件：如果 z 軸超出範圍
    if z > 500:
        running = False

pygame.quit()
