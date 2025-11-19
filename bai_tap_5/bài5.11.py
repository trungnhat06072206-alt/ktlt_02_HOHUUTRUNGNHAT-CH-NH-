print("ho huu trung nhat")
print("mssv 245752021610023")

import numpy as np

# Tạo mảng cấu trúc
students = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
], dtype=[('name', 'U10'), ('class', 'i4'), ('height', 'f4')])

# Sắp xếp theo lớp, sau đó theo chiều cao
sorted_students = np.sort(students, order=['class', 'height'])

print("Kết quả sắp xếp:")
print(sorted_students)
