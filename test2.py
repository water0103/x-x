#y = (-1) ** x = math.exp((2 * k * math.pi + math.pi) * x * 1j)
import math
import pygame
#x with using while
#k with using for i in range

window_size = 800
window = pygame.display.set_mode((window_size, window_size))
clock = pygame.time.Clock()

# 初始化 x 值
number_of_x = -25
points = []

# 計算實部與虛部的函數
def real_imagine_root(x):
    real =math.cos(math.pi * x)    
    imagine =math.sin(math.pi * x)
    return real, imagine


running = True
while running: 
    clock.tick(60)
    window.fill((0, 0, 0))

    real_x, imagine_y = real_imagine_root(number_of_x)
    real_x = real_x * 100 + window_size / 2
    imagine_y = imagine_y * 100 + window_size / 2
    points.append((real_x, imagine_y))

    # 繪製所有計算的浮點數座標點
    for point in points:
        pygame.draw.circle(window, (255, 0, 0), (round(point[0]), round(point[1])), 5)
    number_of_x += 0.01

    if number_of_x > 25:
        break
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()

# 退出 Pygame
pygame.quit()