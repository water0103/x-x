import math
import pygame

# 初始化 Pygame
pygame.init()

# 設定視窗大小
window_size = 800
window = pygame.display.set_mode((window_size, window_size))
clock = pygame.time.Clock()

# 初始 x 值
number_of_x = -25

# 計算實部與虛部的函數
def real_imagine_root(x):
    real = math.cos(math.pi * x)
    imagine = math.sin(math.pi * x)
    return real, imagine

#劃出原點與指定點的直線
def connect_points(i  , points):
    pygame.draw.line(window , (255 , 255 , 255) , (points[i][0] , points[i][1]) , (window_size / 2 , window_size / 2))

# 存放點的列表
points = []

# 主循環
running = True
while running:
    clock.tick(60)
    window.fill((0, 0, 0))
    
    # 計算當前的實部與虛部並記錄點
    real_x, imagine_y = real_imagine_root(number_of_x)
    real_x = real_x * 100 + window_size / 2
    imagine_y = imagine_y * 100 + window_size / 2
    points.append((real_x, imagine_y))
    
    # 繪製所有計算的浮點數座標點
    for point in points:
        pygame.draw.circle(window, (255, 0, 0), (round(point[0]), round(point[1])), 5)
    
    

    # 更新 x 值並限制範圍
    number_of_x += 0.01
    if number_of_x > 25:
        break
    
    # 退出事件處理
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # 更新顯示
    pygame.display.flip()

# 退出 Pygame
pygame.quit()