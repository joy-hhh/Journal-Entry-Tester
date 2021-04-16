import tkinter

def btn_check():
    count = 0

    for i in range(4):
        if ck_val[i].get() == True:
            count = count + 1
            print(LIST[i] + " 항목이 선택")

    print("총 " + str(count) + "개가 체크되었습니다.")
    
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
Radiovar = IntVar()

for i in range(4):
    ck_val[i] = tkinter.BooleanVar()
    ck_val[i].set(False)
    ck_btn[i] = tkinter.Radiobutton(text=LIST[i], font=("System", 20),
                                 variable=Radiovar, value=i)
    ck_btn[i].place(x = 100, y = 150+50*i)

submit = tkinter.Button(text="확인", font=("System", 20), command=btn_check)
submit.place(x = 100, y = 350)
    
win.mainloop()
