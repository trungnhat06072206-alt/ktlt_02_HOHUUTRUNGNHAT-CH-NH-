print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

ds = input("Nhập các số, cách nhau bằng dấu phẩy: ").split(',')
so_le = [int(x) for x in ds if int(x) % 2 != 0]
print("Các số lẻ là:")
print(so_le)
