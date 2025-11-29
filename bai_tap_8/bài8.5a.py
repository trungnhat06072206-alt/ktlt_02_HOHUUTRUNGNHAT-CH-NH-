print("Hồ Hữu Trung Nhật")
print("245752021610023")

import tkinter as tk

root = tk.Tk()
root.title("Radio Button Example")
root.geometry("350x250")

v = tk.IntVar()
v.set(1)  # mặc định chọn Python

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
         text="Choose your favourite programming language:",
         justify=tk.LEFT,
         padx=20
         ).pack()

for text, value in languages:
    tk.Radiobutton(root,
                   text=text,
                   padx=20,
                   variable=v,
                   command=ShowChoice,
                   value=value).pack(anchor=tk.W)

root.mainloop()
