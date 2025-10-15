# Bài 11: Kết nối các danh sách vào từ điển
l = [1, 'python', 4, 7]
k = ['cse', 2, 'guntur', 8]

m = []
m.append(l)
m.append(k)

print("List m:", m)

d = {1: l, 2: k, 'combine_list': m}
print("Dictionary d:", d)
