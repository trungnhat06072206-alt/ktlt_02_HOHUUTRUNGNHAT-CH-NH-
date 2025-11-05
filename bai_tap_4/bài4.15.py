print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

chuoi = input("Nhập chuỗi các từ tiếng Anh: ")
tu = chuoi.split()
tu.sort()
print("Các từ theo thứ tự từ điển là:")
for t in tu:
    print(t)
