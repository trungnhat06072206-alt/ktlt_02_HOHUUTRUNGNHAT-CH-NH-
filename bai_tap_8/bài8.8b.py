print("Hồ Hữu Trung Nhật")
print("245752021610023")

from tkinter import *

window = Tk()
window.title("Welcome")
window.geometry("350x150")

v = IntVar()
v.set(1)   # lựa chọn mặc định

# Tạo radio button
Radiobutton(window, text="First", variable=v, value=1).pack(anchor=W)
Radiobutton(window, text="Second", variable=v, value=2).pack(anchor=W)
Radiobutton(window, text="Third", variable=v, value=3).pack(anchor=W)

def show_choice():
    print("Bạn chọn:", v.get())

Button(window, text="Click Me", command=show_choice).pack(pady=10)

window.mainloop()
