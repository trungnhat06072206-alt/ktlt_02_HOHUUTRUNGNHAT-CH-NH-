print("ho huu trung nhat")
print("mssv 245752021610023")

class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

# Test
aCircle = Circle(2)
print("Diện tích hình tròn:", aCircle.area())
