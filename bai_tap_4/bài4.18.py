print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

n = int(input("Nhập n: "))
fibo = [0, 1]
while fibo[-1] + fibo[-2] < n:
    fibo.append(fibo[-1] + fibo[-2])
print("Các số Fibonacci nhỏ hơn", n, "là:")
print(fibo)
