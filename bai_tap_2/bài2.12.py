# Bài 12: Kiểm tra mật khẩu hợp lệ
import re

# Nhập nhiều mật khẩu, cách nhau bằng dấu phẩy
items = [x for x in input("Nhập các mật khẩu, cách nhau bằng dấu phẩy: ").split(',')]
valid_passwords = []

for p in items:
    # Loại bỏ khoảng trắng thừa
    p = p.strip()

    # Kiểm tra độ dài
    if len(p) < 6 or len(p) > 12:
        continue
    # Kiểm tra ký tự thường
    if not re.search("[a-z]", p):
        continue
    # Kiểm tra chữ số
    if not re.search("[0-9]", p):
        continue
    # Kiểm tra ký tự hoa
    if not re.search("[A-Z]", p):
        continue
    # Kiểm tra ký tự đặc biệt
    if not re.search("[$#@]", p):
        continue

    # Nếu qua tất cả điều kiện -> hợp lệ
    valid_passwords.append(p)

print("✅ Các mật khẩu hợp lệ là:", ", ".join(valid_passwords))
