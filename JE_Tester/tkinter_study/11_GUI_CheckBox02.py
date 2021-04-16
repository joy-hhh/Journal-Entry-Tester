import tkinter

def btn_check():
    if ck_val.get() == True:
        print("버튼이 체크 되었습니다.")
    else:
        print("버튼이 체크 되지 않았습니다.")
        
win = tkinter.Tk()
win.title("체크 버튼 만들기")
win.geometry("400x400")

ck_val = tkinter.BooleanVar()
ck_val.set(False)

ck_btn = tkinter.Checkbutton(text="체크 버튼", font=("System", 20),
                             variable=ck_val, command=btn_check)
ck_btn.pack()

win.mainloop()
