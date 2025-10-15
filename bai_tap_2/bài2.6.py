# Bài 6: In các số chia hết cho 7 nhưng không chia hết cho 5 từ 2000 đến 3200
result = []

for i in range(2000, 3201):  # 3201 vì range dừng trước giới hạn cuối
    if (i % 7 == 0) and (i % 5 != 0):
        result.append(str(i))

print(", ".join(result))
