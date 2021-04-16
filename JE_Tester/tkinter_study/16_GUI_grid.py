import tkinter

win = tkinter.Tk()
win.title("파이썬 Grid 이해")
win.geometry("400x300")

label1 = tkinter.Label(win,text="이름 입력")
label2 = tkinter.Label(win,text="패스워드 입력")
label1.grid(row=0, column=0)
label2.grid(row=1, column=0)

text1 = tkinter.Text(win)
text2 = tkinter.Text(win)
text1.grid(row=0, column=1)
text2.grid(row=1, column=1)

button1 = tkinter.Button(win, text="확인")
button2 = tkinter.Button(win, text="취소")
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)

win.mainloop()
