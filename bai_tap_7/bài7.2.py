print("Sinh viên: Ho Huu Trung Nhat")
print("MSSV: 245752021610023")

k = open("b.txt", "r")

char = 0
wc = 0
lc = 0

for line in k:
    for c in line:
        char += 1
        if c == " ":
            wc += 1
        if c == "\n":
            wc += 1
            lc += 1

print("The no. of chars is %d\nThe no. of words is %d\nThe no. of lines is %d"
      % (char, wc, lc))
