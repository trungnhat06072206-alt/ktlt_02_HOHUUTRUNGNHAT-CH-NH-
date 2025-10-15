# Bài 7: Tạo dictionary chứa (i, i*i)
n = int(input("Nhập vào một số nguyên n: "))
d = {}

for i in range(1, n + 1):
    d[i] = i * i

print(d)
