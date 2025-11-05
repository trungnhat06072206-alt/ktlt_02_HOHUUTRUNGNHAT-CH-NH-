print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

chuoi = input("Nhập chuỗi các số nhị phân (4 chữ số, cách nhau bằng dấu phẩy): ")
day = chuoi.split(',')
ket_qua = []

for so in day:
    if int(so, 2) % 5 == 0:
        ket_qua.append(so)

print("Các số nhị phân chia hết cho 5 là:")
print(','.join(ket_qua))
