print("Sinh viên: Hồ Hữu Trung Nhật")
print("MSSV: 245752021610023")

import tkinter
import random

# danh sách màu
colours = ['Red', 'Blue', 'Green', 'Pink', 'Black',
           'Yellow', 'Orange', 'White', 'Purple', 'Brown']

score = 0
timeleft = 120      # đổi từ 30 giây ➜ 120 giây (Bước 2)


# ------------------------ BẮT ĐẦU GAME ------------------------
def startGame(event):
    if timeleft == 120:
        countdown()
    nextColour()


# ------------------------ CHỌN MÀU MỚI ------------------------
def nextColour():
    global score
    global timeleft

    if timeleft > 0:

        e.focus_set()

        # kiểm tra kết quả người chơi nhập
        if e.get().lower() == colours[1].lower():
            score += 2        # đúng +2 điểm  (Bước 3)
        else:
            if e.get() != "":
                score -= 1    # sai -1 điểm (Bước 3)

        # xóa khung nhập
        e.delete(0, tkinter.END)

        # xáo trộn màu
        random.shuffle(colours)

        # thay đổi label hiển thị
        label.config(fg=str(colours[1]), text=str(colours[0]))

        # cập nhật điểm
        scoreLabel.config(text="Score: " + str(score))


# ------------------------ ĐẾM NGƯỢC ------------------------
def countdown():
    global timeleft

    if timeleft > 0:
        timeleft -= 1

        timeLabel.config(text="Time left: " + str(timeleft))

        # gọi lại sau mỗi 1000ms = 1 giây
        timeLabel.after(1000, countdown)


# ------------------------ GIAO DIỆN TKINTER ------------------------
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")

instructions = tkinter.Label(root,
                             text="Type in the colour of the words, not the text",
                             font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press Enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: " + str(timeleft),
                          font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 60))
label.pack()

# ô nhập
e = tkinter.Entry(root)
e.pack()

# nhấn Enter để chơi
root.bind('<Return>', startGame)

e.focus_set()
root.mainloop()
