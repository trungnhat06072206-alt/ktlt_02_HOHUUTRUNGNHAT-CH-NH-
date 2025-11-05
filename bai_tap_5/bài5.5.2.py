print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

import listmath

# Nhập danh sách số nguyên
ds = list(map(int, input("Nhập các số cách nhau bằng dấu cách: ").split()))

lon_nhat = listmath.find_max(ds)
nho_nhat = listmath.find_min(ds)

print("Phần tử lớn nhất là:", lon_nhat)
print("Phần tử nhỏ nhất là:", nho_nhat)
