# Bài 10: Tính chu vi và diện tích hình tròn

import math

def Tinh(R):
    chu_vi = 2 * math.pi * R
    dien_tich = math.pi * R ** 2
    return chu_vi, dien_tich

R = float(input("Nhập bán kính R: "))
cv, dt = Tinh(R)
print(f"Chu vi = {cv:.2f}")
print(f"Diện tích = {dt:.2f}")
