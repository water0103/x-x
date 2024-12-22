import pygame
import numpy as np
import math
import random

# 初始化 Pygame
pygame.init()

# 視窗大小
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D to 2D Projection")

# 建立投影矩陣函數
def build_projection_matrix(fov, aspect, zn, zf):
    proj = np.zeros((4, 4), dtype=float)
    proj[0][0] = 1 / (np.tan(fov * 0.5) * aspect)
    proj[1][1] = 1 / np.tan(fov * 0.5)
    proj[2][2] = zf / (zf - zn)
    proj[2][3] = 1.0
    proj[3][2] = (zn * zf) / (zn - zf)
    return proj

# 投影 3D 點到 2D
def project_point_to_2d(matrix, point, screen_width, screen_height):
    vec = np.array([point[0], point[1], point[2], 1.0])
    projected = np.dot(matrix, vec)
    if projected[3] != 0:
        projected /= projected[3]
    x_screen = (projected[0] + 1) * 0.5 * screen_width
    y_screen = (1 - projected[1]) * 0.5 * screen_height
    return int(x_screen), int(y_screen)

# 設定投影參數
fov = math.radians(45)  # 視場角
aspect = screen_width / screen_height  # 長寬比
zn = 0.1  # 近剪裁面
zf = 100.0  # 遠剪裁面

# 建立投影矩陣
proj_matrix = build_projection_matrix(fov, aspect, zn, zf)

# 隨機生成多個 3D 世界座標點
points_3d = [[random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(0.5, 20)] for _ in range(10)]

# 投影到 2D
points_2d = [project_point_to_2d(proj_matrix, point, screen_width, screen_height) for point in points_3d]

# 主迴圈
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 填充背景
    screen.fill((30, 30, 30))

    # 畫原始 3D 點
    for point in points_3d:
        x, y, z = point
        screen_x = int((x + 5) * 50)  # 簡單平移以可視化
        screen_y = int((5 - y) * 50)
        pygame.draw.circle(screen, (0, 255, 0), (screen_x, screen_y), 5)

    # 畫投影後的 2D 點
    for point in points_2d:
        pygame.draw.circle(screen, (255, 255, 255), point, 5)

    # 顯示文字
    font = pygame.font.Font(None, 36)
    text_3d = font.render("Green: 3D World Points", True, (0, 255, 0))
    text_2d = font.render("Red: Projected 2D Points", True, (255, 255, 255))
    screen.blit(text_3d, (10, 10))
    screen.blit(text_2d, (10, 50))

    # 更新螢幕
    pygame.display.flip()

# 結束 Pygame
pygame.quit()
