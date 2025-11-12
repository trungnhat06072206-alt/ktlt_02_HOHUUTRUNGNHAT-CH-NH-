print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

def Sequential_Search(dlist, item):
    pos = 0
    found = False

    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1

    if found:
        return True, pos
    else:
        return False, -1
