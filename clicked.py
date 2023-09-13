import time
import pyautogui

# 假设这是你的9个点的坐标
points = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x9, y9)]

while True:
    for point in points:
        pyautogui.click(point)
    time.sleep(1800)  # 每隔30分钟（1800秒）执行一次
