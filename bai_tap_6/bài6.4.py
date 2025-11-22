print("ho huu trung nhat")
print("mssv 245752021610023")

class py_solution:
    def roman_to_int(self, s):
        rom_val = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        int_val = 0

        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val

# Test
p = py_solution()
print(p.roman_to_int('MMIV'))
print(p.roman_to_int('MCMXLIV'))
