# Bài 18: Loại bỏ ký tự số khỏi chuỗi

s = input("Nhập chuỗi: ")
kq = ''.join(ch for ch in s if not ch.isdigit())
print("Chuỗi sau khi loại bỏ số:", kq)
