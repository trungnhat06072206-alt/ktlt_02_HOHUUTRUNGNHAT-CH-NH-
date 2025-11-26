print("hồ hữu trung nhật")
print("sv 245752021610023")

def write_list_to_file(filename, data_list):
    with open(filename, "w", encoding="utf-8") as f:
        for item in data_list:
            f.write(str(item) + "\n")

write_list_to_file("output.txt", ["Python", "File", "Exercise"])
