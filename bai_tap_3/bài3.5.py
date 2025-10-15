# Bài 5: Sử dụng biến toàn cục (global)
a = "Hello Guy!"

def say():
    global a
    a = "Vinh University"
    print(a)

say()
print(a)
