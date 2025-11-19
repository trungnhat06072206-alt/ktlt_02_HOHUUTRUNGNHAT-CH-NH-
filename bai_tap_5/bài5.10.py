print("ho huu trung nhat")
print("mssv 245752021610023")

def bubbleSort(nlist):
    loop = len(nlist)

    for i in range(loop - 1):
        swapped = False

        for j in range(loop - 1 - i):
            
            if nlist[j] > nlist[j + 1]:

                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True


        if not swapped:
            break

    return nlist


data = input("Nhập danh sách số, cách nhau bởi dấu phẩy: ")

nlist = [int(x.strip()) for x in data.split(",")]

sorted_list = bubbleSort(nlist)

print("Danh sách sau khi sắp xếp:", sorted_list)
