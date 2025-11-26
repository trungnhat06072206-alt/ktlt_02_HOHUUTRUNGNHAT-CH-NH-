print("hồ hữu trung nhật")
print("sv 245752021610023")

def find_longest_words(filename):
    with open(filename, "r", encoding="utf-8") as f:
        words = f.read().split()

    max_len = max(len(w) for w in words)
    longest_words = [w for w in words if len(w) == max_len]
    return longest_words

print("Từ dài nhất:", find_longest_words("b.txt"))
