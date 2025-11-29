print("Hồ Hữu Trung Nhật")
print("245752021610023")

from tkinter import *

# Tạo cửa sổ
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("350x200")

# Thêm label
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

# Hàm xử lý khi nhấn nút
def clicked():
    lbl.configure(text="Button was clicked !!!")

# Nút bấm
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)

window.mainloop()
