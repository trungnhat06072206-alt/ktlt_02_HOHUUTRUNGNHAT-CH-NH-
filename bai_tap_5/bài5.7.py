print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]

students_details = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

students = np.array(students_details, dtype=data_type)

print("Mảng ban đầu:")
print(students)

sorted_students = np.sort(students, order='height')
print("\nMảng sau khi sắp xếp theo chiều cao:")
print(sorted_students)
