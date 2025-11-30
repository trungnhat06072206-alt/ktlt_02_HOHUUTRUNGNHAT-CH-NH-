print("Hồ Hữu Trung Nhật")
print("245752021610023")

from tkinter import *

window = Tk()
window.title("Thông tin cá nhân")
window.geometry("350x250")

Label(window, text="Họ và tên: Hồ Hữu Trung Nhật").pack(anchor=W, pady=5)
Label(window, text="Ngày sinh: 06/07/2006").pack(anchor=W, pady=5)
Label(window, text="MSSV: 245752021610023").pack(anchor=W, pady=5)
Label(window, text="Ngành học: Kỹ thuật điều khiển và tự động hóa").pack(anchor=W, pady=5)

window.mainloop()
