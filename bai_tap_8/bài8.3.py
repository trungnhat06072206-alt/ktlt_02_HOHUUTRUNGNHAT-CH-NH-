print("Hồ Hữu Trung Nhật")
print("245752021610023")

import turtle
import random

colors = ["red", "green", "blue", "orange", "purple"]

p = turtle.Turtle()
p.speed(0)
p.pensize(3)

# Vẽ 12 vòng tròn, mỗi lần quay 30 độ
for i in range(12):
    p.pencolor(random.choice(colors))
    p.circle(100)
    p.left(30)

turtle.done()
