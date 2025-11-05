print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

so_tien = 0
print("Nhập nhật ký giao dịch (D n để gửi, W n để rút, Enter để dừng):")

while True:
    nhap = input()
    if not nhap:
        break
    lenh = nhap.split()
    if lenh[0] == 'D':
        so_tien += int(lenh[1])
    elif lenh[0] == 'W':
        so_tien -= int(lenh[1])

print("Số tiền thực có trong tài khoản là:", so_tien)
