print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

import search_module

# Nhập số phần tử
n = int(input("Nhập số lượng phần tử trong danh sách: "))
dlist = []

# Nhập danh sách
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    dlist.append(value)

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm
found, pos = search_module.Sequential_Search(dlist, item)

print("Danh sách vừa nhập:", dlist)
if found:
    print(f"Phần tử {item} được tìm thấy tại vị trí {pos}")
else:
    print(f"Phần tử {item} không có trong danh sách")
