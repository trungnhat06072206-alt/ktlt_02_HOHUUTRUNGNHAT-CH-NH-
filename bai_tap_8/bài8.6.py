print("Sinh viên: Ho Huu Trung Nhat")
print("MSSV: 245752021610023")

from tkinter import *
from tkinter import messagebox


# ===========================
# Bước 3: Các hàm xử lý menu
# ===========================
def NewFile():
    messagebox.showinfo("New File", "Bạn đã chọn New File!")

def OpenFile():
    messagebox.showinfo("Open File", "Bạn đã chọn Open File!")

def Exit():
    root.quit()

def InsText():
    messagebox.showinfo("Insert Text", "Bạn đã chọn Insert → Text")

def InsPic():
    messagebox.showinfo("Insert Picture", "Bạn đã chọn Insert → Picture")

def About():
    messagebox.showinfo("About", "This is a simple example of a menu!")


# ===========================
# Bước 1: Tạo cửa sổ và menu cơ bản
# ===========================
root = Tk()
root.title("Menu Example")
root.geometry("400x300")

menu = Menu(root)
root.config(menu=menu)

# Menu File
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)
filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# Menu Insert (bổ sung theo bước 2)
insertmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Insert", menu=insertmenu)
insertmenu.add_command(label="Text", command=InsText)
insertmenu.add_command(label="Picture", command=InsPic)

# Menu Help
helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=About)


# ===========================
# Chạy chương trình
# ===========================
root.mainloop()
