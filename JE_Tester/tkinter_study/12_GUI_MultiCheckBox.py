import tkinter


win = tkinter.Tk()
win.title("멀티 체크 버튼 만들기")
win.geometry("400x400")

#멀티 목록 정의
LIST = ["파이썬 입문 과정",
        "노션 활용 방법",
        "모의해킹 실무 과정",
        "마인크래프트 파이썬"]

ck_val = [None]*4
ck_btn = [None]*4

for i in range(4):
    ck_val[i] = tkinter.BooleanVar()
    ck_val[i].set(False)
    ck_btn[i] = tkinter.Checkbutton(text=LIST[i], font=("System", 20),
                                 variable=ck_val[i])
    ck_btn[i].place(x = 100, y = 150+50*i)
    
win.mainloop()
