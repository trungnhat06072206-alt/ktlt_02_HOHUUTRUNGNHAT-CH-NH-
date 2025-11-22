print("ho huu trung nhat")
print("mssv 245752021610023")

class py_solution:
    def reverse_words(self, s):
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

# Test
p = py_solution()
print(p.reverse_words("hello .py"))
