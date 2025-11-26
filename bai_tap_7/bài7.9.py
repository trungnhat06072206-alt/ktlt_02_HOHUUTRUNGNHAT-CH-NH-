print("hồ hữu trung nhật")
print("sv 245752021610023")

def copy_file(src, dst):
    with open(src, "r", encoding="utf-8") as f1:
        with open(dst, "w", encoding="utf-8") as f2:
            f2.write(f1.read())

copy_file("b.txt", "copy_test.txt")
