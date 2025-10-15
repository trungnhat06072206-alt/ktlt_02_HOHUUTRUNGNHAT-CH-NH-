# Bài 13: Giải phương trình bậc hai ax^2 + bx + c = 0
import math

print("Giải phương trình bậc hai: ax^2 + bx + c = 0")

a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
c = float(input("Nhập c = "))

if a == 0:
    # Trường hợp a = 0 -> phương trình bậc nhất
    if b == 0:
        print("Phương trình vô nghiệm!" if c != 0 else "Phương trình có vô số nghiệm!")
    else:
        x = -c / b
        print("Phương trình có một nghiệm duy nhất x =", x)
else:
    # Tính delta
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x1 = x2 =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
