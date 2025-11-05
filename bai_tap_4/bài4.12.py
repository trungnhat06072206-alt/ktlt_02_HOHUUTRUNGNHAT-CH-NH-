print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

ds = input("Nhập list: ").split()
if 'không' in ds:
    ds.remove('không')
print("List sau khi xóa phần tử 'không' (nếu có):")
for ch in ds:
    print(ch)
