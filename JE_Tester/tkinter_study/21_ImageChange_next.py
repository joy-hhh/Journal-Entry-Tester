from tkinter import *

num = 0
def forward_image():
    global num
    num = num - 1
    label_Img.configure(image=py_Img[num])
    
def next_image():
    global num
    num = num + 1
    label_Img.configure(image=py_Img[num])

win = Tk()
win.title("이미지 버튼별 표시.")

py_Img = [PhotoImage(file="img/01.png"),
          PhotoImage(file="img/02.png"),
          PhotoImage(file="img/03.png"),
          PhotoImage(file="img/04.png")]

label_Img = Label(win, image=py_Img[0])
label_Img.pack()

button = Button(win, text="이전", command=forward_image)
button.pack()

button = Button(win, text="다음", command=next_image)
button.pack()

win.mainloop()
