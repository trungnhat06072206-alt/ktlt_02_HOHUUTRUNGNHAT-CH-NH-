print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

cau = input("Nhập câu: ")
chu_hoa = 0
chu_thuong = 0

for ch in cau:
    if ch.isupper():
        chu_hoa += 1
    elif ch.islower():
        chu_thuong += 1

print("Chữ hoa:", chu_hoa)
print("Chữ thường:", chu_thuong)
