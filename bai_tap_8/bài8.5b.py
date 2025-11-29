print("Hồ Hữu Trung Nhật")
print("245752021610023")

import tkinter as tk

root = tk.Tk()
root.title("Indicator Style Example")
root.geometry("350x300")

v = tk.IntVar()
v.set(1)   # chọn mặc định

languages = [
    ("Python", 1),
    ("Perl", 2),
    ("Java", 3),
    ("C++", 4),
    ("C", 5)
]

def ShowChoice():
    print("Bạn chọn:", v.get())

tk.Label(root,
         text="Choose your favourite programming language",
         pady=10).pack()

for text, value in languages:
    tk.Radiobutton(root,
                   text=text,
                   variable=v,
                   value=value,
                   command=ShowChoice,
                   indicatoron=0,      # tắt dấu radio, tạo dạng nút
                   width=20,
                   padx=10,
                   pady=5).pack(pady=3)

root.mainloop()
