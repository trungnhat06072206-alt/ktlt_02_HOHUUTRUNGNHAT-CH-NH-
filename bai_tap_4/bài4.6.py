# Bài 17: Nhập họ tên và tách riêng

hoten = input("Nhập họ tên: ")
parts = hoten.split()
print("Họ:", parts[0])
print("Tên:", parts[-1])
