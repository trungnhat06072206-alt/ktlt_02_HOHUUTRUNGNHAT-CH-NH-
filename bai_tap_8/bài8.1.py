print("Hồ Hữu Trung Nhật")
print("245752021610023")

import turtle

window = turtle.Screen()
window.bgcolor("lightgreen")

painter = turtle.Turtle()
painter.fillcolor("blue")
painter.pencolor("blue")
painter.pensize(3)

def drawSquare(t, size):
    for i in range(4):
        t.forward(size)
        t.left(90)

for i in range(18):
    painter.left(20)
    drawSquare(painter, 200)

window.mainloop()
