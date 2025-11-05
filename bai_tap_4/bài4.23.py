print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

cau = input("Nhập câu: ")
so_chu = 0
so_so = 0

for ch in cau:
    if ch.isalpha():
        so_chu += 1
    elif ch.isdigit():
        so_so += 1

print("Số chữ cái là:", so_chu)
print("Số chữ số là:", so_so)
