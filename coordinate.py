from pynput import mouse

def on_move(x, y):
    print('鼠标位置：({0}, {1})'.format(x, y))

# 创建并启动鼠标监听器
with mouse.Listener(on_move=on_move) as listener:
    listener.join()
