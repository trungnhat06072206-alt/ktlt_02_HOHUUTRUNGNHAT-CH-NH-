# Bài 11: Tính lãi suất tiết kiệm

def benefit(P, n, r):
    return P * ((1 + r/100) ** n)

P = float(input("Nhập số tiền ban đầu: "))
n = int(input("Nhập số năm gửi: "))
r = float(input("Nhập lãi suất (%/năm): "))

print(f"Số tiền nhận được sau {n} năm là: {benefit(P, n, r):.2f}")
