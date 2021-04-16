import tkinter

win = tkinter.Tk()
win.title("체크 버튼 만들기")
win.geometry("400x400")

ck_val = tkinter.BooleanVar()
ck_val.set(True)

ck_btn = tkinter.Checkbutton(text="체크 버튼", font=("System", 20), variable=ck_val)
ck_btn.pack()

win.mainloop()
