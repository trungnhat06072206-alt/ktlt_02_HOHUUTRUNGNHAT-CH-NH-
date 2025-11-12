print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

def binary_search(lst, value):
    lowerBound = 0
    upperBound = len(lst) - 1
    found = False

    while lowerBound <= upperBound and not found:
        midPoint = (lowerBound + upperBound) // 2
        if lst[midPoint] == value:
            found = True
        elif value < lst[midPoint]:
            upperBound = midPoint - 1
        else:
            lowerBound = midPoint + 1

    return found
