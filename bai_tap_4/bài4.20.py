print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

n = int(input("Nhập số dòng n: "))

def pascal(n):
    tamgiac = []
    for i in range(n):
        hang = [1] * (i + 1)
        for j in range(1, i):
            hang[j] = tamgiac[i - 1][j - 1] + tamgiac[i - 1][j]
        tamgiac.append(hang)
    return tamgiac

for hang in pascal(n):
    print(hang)
