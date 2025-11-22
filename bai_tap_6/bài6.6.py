print("ho huu trung nhat")
print("mssv 245752021610023")

class IOString:
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input("Nhập chuỗi: ")

    def print_String(self):
        print(self.s.upper())

# Test
str1 = IOString()
str1.get_String()
str1.print_String()
