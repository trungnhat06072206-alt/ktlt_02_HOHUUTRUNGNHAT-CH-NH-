print("Sinh viên: Ho Huu Trung Nhat")
print("MSSV: 245752021610023")

with open("b.txt", "a") as myfile:
    myfile.write("\nPython Exercises\n")
    myfile.write("Java Exercises\n")

with open("b.txt") as f:
    print(f.read())
