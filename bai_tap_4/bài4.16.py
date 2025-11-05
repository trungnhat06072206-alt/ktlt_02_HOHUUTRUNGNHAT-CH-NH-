print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

chuoi = input("Nhập chuỗi các số nhị phân (cách nhau bằng dấu phẩy): ")
day = chuoi.split(',')
print("Giá trị thập phân của các số vừa nhập là:")
for so in day:
    print(f"{so} = {int(so, 2)}")
