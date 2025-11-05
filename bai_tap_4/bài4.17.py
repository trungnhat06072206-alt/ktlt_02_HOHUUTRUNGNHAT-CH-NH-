print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

n = int(input("Nhập n: "))
print("Các số có tổng ước lớn hơn chính nó là:")
for i in range(1, n + 1):
    tong_uoc = sum(j for j in range(1, i) if i % j == 0)
    if tong_uoc > i:
        print(i)
