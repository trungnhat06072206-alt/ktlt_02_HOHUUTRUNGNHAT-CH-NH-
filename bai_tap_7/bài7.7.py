print("hồ hữu trung nhật")
print("sv 245752021610023")

def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())

print("Số dòng:", count_lines("b.txt"))
