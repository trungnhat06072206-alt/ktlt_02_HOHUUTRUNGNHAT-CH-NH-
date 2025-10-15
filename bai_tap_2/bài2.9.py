# Bài 9: Đếm số ký tự trong chuỗi
s = input("Enter a string: ")
char_count = {}

for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

print("Character frequency:", char_count)
