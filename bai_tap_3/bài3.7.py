# Bài 7: Kiểm tra số chẵn hay lẻ

def checkValue(n):
    if n % 2 == 0:
        print("Đây là một số chẵn")
    else:
        print("Đây là một số lẻ")

# --- Chạy thử ---
n = int(input("Nhập một số nguyên: "))
checkValue(n)
