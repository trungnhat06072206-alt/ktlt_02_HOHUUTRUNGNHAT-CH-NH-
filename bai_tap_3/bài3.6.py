# Bài 6: Truyền tham số vào hàm
def get_sum(*num):  # Dấu * cho phép truyền nhiều đối số
    tmp = 0
    for i in num:
        tmp += i
    return tmp

result = get_sum(1, 2, 3, 4, 5)
print("Tổng các tham số là:", result)
