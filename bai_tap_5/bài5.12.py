print("ho huu trung nhat")
print("mssv 245752021610023")

import numpy as np

student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.])

# Sắp xếp theo nhiều cột: chiều cao tăng, sau đó id tăng
index_sorted = np.lexsort((student_id, student_height))

print("Chỉ số sắp xếp:")
print(index_sorted)

print("Dữ liệu sau khi sắp xếp:")
for i in index_sorted:
    print(student_id[i], student_height[i])
