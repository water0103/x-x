import matplotlib.pyplot as plt
import numpy as np

# 建立投影矩陣函數
def build_projection_matrix(fov, aspect, zn, zf):
    proj = np.zeros((4, 4), dtype=float)
    proj[0][0] = 1 / (np.tan(fov * 0.5) * aspect)
    proj[1][1] = 1 / np.tan(fov * 0.5)
    proj[2][2] = zf / (zf - zn)
    proj[2][3] = 1.0
    proj[3][2] = (zn * zf) / (zn - zf)
    return proj

# 投影 3D 點到螢幕座標
def project_point_to_2d(matrix, point, screen_width, screen_height):
    vec = np.array([point[0], point[1], point[2], 1.0])
    projected = np.dot(matrix, vec)
    if projected[3] != 0:
        projected /= projected[3]
    x_screen = (projected[0] + 1) * 0.5 * screen_width
    y_screen = (1 - projected[1]) * 0.5 * screen_height
    return x_screen, y_screen

# 設定參數
fov = np.radians(45)  # 視場角
aspect = 16 / 9       # 長寬比
zn = 0.1              # 近剪裁面
zf = 100.0            # 遠剪裁面

# 建立投影矩陣
proj_matrix = build_projection_matrix(fov, aspect, zn, zf)

# 定義多個 3D 世界座標點
points_3d = np.array([
    [1, 1, 2],
    [-1, -1, 2],
    [0, 0, 5],
    [2, 2, 10],
    [-2, -2, 10],
    [0, 1, 0.5]
])

# 螢幕尺寸
screen_width = 1920
screen_height = 1080

# 投影 3D 點到 2D
points_2d = np.array([project_point_to_2d(proj_matrix, point, screen_width, screen_height) for point in points_3d])

# 畫圖
fig, axes = plt.subplots(1, 2, figsize=(12, 6), subplot_kw={'projection': None})

# 左圖：3D 世界座標
ax_3d = axes[0]
ax_3d.scatter(points_3d[:, 0], points_3d[:, 1], color='blue', label='3D Points')
ax_3d.axhline(0, color='black', linewidth=0.5)
ax_3d.axvline(0, color='black', linewidth=0.5)
ax_3d.set_title("3D World Coordinates")
ax_3d.set_xlabel("X")
ax_3d.set_ylabel("Y")
ax_3d.grid(True)

# 右圖：2D 螢幕座標
ax_2d = axes[1]
ax_2d.scatter(points_2d[:, 0], points_2d[:, 1], color='red', label='Projected 2D Points')
ax_2d.axhline(screen_height / 2, color='black', linewidth=0.5)
ax_2d.axvline(screen_width / 2, color='black', linewidth=0.5)
ax_2d.set_xlim(0, screen_width)
ax_2d.set_ylim(screen_height, 0)  # Y 軸反轉
ax_2d.set_title("2D Screen Coordinates")
ax_2d.set_xlabel("Screen X")
ax_2d.set_ylabel("Screen Y")
ax_2d.grid(True)

plt.tight_layout()
plt.show()
