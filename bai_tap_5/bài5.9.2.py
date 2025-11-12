print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

import binary_module

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử trong danh sách (đã sắp xếp): "))
lst = []

# Nhập danh sách
for i in range(n):
    value = int(input(f"Nhập phần tử thứ {i+1}: "))
    lst.append(value)

# Đảm bảo danh sách được sắp xếp
lst.sort()

# Nhập giá trị cần tìm
item = int(input("Nhập giá trị cần tìm: "))

# Gọi hàm tìm kiếm nhị phân
found = binary_module.binary_search(lst, item)

print("Danh sách (đã sắp xếp):", lst)
if found:
    print(f"✅ Phần tử {item} có trong danh sách.")
else:
    print(f"❌ Phần tử {item} không có trong danh sách.")
