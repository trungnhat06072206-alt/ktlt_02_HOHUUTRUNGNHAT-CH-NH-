# Bài 8: In dãy Fibonacci nhỏ hơn 4.000.000 và tính tổng các số chẵn
a, b = 0, 1
even_sum = 0

print("Fibonacci sequence (under 4,000,000):")

while a < 4000000:
    print(a, end=" ")
    if a % 2 == 0:
        even_sum += a
    a, b = b, a + b

print("\nTổng các số chẵn trong dãy là:", even_sum)
