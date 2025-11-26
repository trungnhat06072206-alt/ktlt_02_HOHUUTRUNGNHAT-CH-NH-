print("hồ hữu trung nhật")
print("sv 245752021610023")

import os

def file_read_from_tail(fname, lines):
    bufsize = 8192
    filesize = os.path.getsize(fname)
    i = 0
    data = []

    with open(fname, "r", encoding="utf-8") as f:
        if bufsize > filesize:
            bufsize = filesize - 1

        while True:
            i += 1
            f.seek(filesize - bufsize * i)
            data.extend(f.readlines())

            if len(data) >= lines or f.tell() == 0:
                print("".join(data[-lines:]))
                break

file_read_from_tail("b.txt", 2)
