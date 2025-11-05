print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

chuoi = input("Nhập dãy các từ: ").split()
max_len = max(len(tu) for tu in chuoi)
print("Các từ dài nhất là:")
for tu in chuoi:
    if len(tu) == max_len:
        print(tu)
