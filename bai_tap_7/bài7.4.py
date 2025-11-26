print("Sinh viên: Ho Huu Trung Nhat")
print("MSSV: 245752021610023")

from itertools import islice

def file_read_from_head(filename, nlines):
    with open(filename) as f:
        for line in islice(f, nlines):
            print(line.rstrip())

file_read_from_head("b.txt", 2)
