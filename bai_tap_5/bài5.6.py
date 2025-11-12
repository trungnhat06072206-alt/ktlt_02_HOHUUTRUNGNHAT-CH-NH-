print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

import listmath

numbers = []
n = int(input("Nhập số lượng phần tử: "))

for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    numbers.append(value)

print("Danh sách vừa nhập:", numbers)

max_value = listmath.find_max(numbers)
min_value = listmath.find_min(numbers)

print("Phần tử lớn nhất:", max_value, "ở vị trí", numbers.index(max_value))
print("Phần tử nhỏ nhất:", min_value, "ở vị trí", numbers.index(min_value))
