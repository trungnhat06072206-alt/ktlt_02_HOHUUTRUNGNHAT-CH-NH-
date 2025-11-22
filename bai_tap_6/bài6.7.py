print("ho huu trung nhat")
print("mssv 245752021610023")

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def circumference(self):
        return 2 * 3.14 * self.radius

# Test
c = Circle(5)
print("Diện tích hình tròn:", c.area())
print("Chu vi hình tròn:", c.circumference())
