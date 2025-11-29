print("Hồ Hữu Trung Nhật")
print("245752021610023")

import turtle, random

colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]

painter = turtle.Turtle()
painter.pensize(3)

for i in range(10):
    color = random.choice(colors)
    painter.pencolor(color)
    painter.circle(100)
    painter.left(36)

painter.setposition(0, 0)
turtle.mainloop()
