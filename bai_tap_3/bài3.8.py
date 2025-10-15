# Bài 8: Robot di chuyển trong mặt phẳng bắt đầu từ (0,0)

import math

pos = [0, 0]
print("Nhập hướng di chuyển (UP/DOWN/LEFT/RIGHT + số bước). Bấm Enter để dừng:")

while True:
    s = input()
    if not s:
        break
    direction, steps = s.split()
    steps = int(steps)

    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps

distance = round(math.sqrt(pos[0] ** 2 + pos[1] ** 2))
print("Khoảng cách từ điểm đầu đến vị trí hiện tại là:", distance)
