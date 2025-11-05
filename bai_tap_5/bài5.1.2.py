print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

import mymath  # import module vừa tạo

values = [2, 4, 6, 8, 10]

print("Squares:")
for v in values:
    print(mymath.square(v))

print("Cubes:")
for v in values:
    print(mymath.cube(v))

print("Average:", mymath.average(values))
