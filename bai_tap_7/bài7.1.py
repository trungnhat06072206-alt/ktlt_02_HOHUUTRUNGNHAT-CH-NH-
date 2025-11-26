print("Sinh viên: Ho Huu Trung Nhat")
print("MSSV: 245752021610023")

input_file = open("b.txt", "r")

for line in input_file:
    line = line.rstrip("\n")
    s = ""
    i = 0
    while i < len(line):
        s = line[i] + s
        i += 1
    print(s)

input_file.close()
