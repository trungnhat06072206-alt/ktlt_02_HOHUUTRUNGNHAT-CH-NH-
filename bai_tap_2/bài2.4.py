# Bài 4: In số nghịch đảo của dãy số tự nhiên trong khoảng (a, b)
a = int(input("Enter value a ---> "))
b = int(input("Enter value b ---> "))

print("Number\tReciprocal (1/n)")
for i in range(a, b + 1):
    if i != 0:
        print(i, "\t", round(1 / i, 4))
    else:
        print(i, "\t Undefined (division by zero)")
