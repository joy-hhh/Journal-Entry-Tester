import tkinter

def btn_check():
    count = 0
    price_sum = 0
    for i in range(4):
        if ck_val[i].get() == True:
            count = count + 1
            price_sum = price_sum + PRICE[i]
            text.insert("1.0", LIST[i] + " 항목이 선택\n")
            #print(LIST[i] + " 항목이 선택")
            
    #1.0은 첫번째 입력, end는 마지막에 입력에 의미
    text.insert("end", "총" + str(count) + "개가 체크되었습니다.\n")
    text.insert("end", "총 결제 금액은" +  str(price_sum) + "입니다.")
    
    #print("총 " + str(count) + "개가 체크되었습니다.")
    
win = tkinter.Tk()
win.title("멀티 체크 버튼 만들기")
win.geometry("500x500")

#멀티 목록 정의
LIST = ["파이썬 입문 과정",
        "노션 활용 방법",
        "모의해킹 실무 과정",
        "마인크래프트 파이썬"]

PRICE = [100000,150000,400000,50000]

ck_val = [None]*4
ck_btn = [None]*4

#라벨 붙이기
label = tkinter.Label(text="과목을 선택 후 확인을 클릭하세요.", font=("System",20))
label.place(x = 100, y = 20)

#텍스트  붙이기
text = tkinter.Text(width=40, height=5, font=("System",20))
text.place(x = 100, y = 50)

for i in range(4):
    ck_val[i] = tkinter.BooleanVar()
    ck_val[i].set(False)
    ck_btn[i] = tkinter.Checkbutton(text=LIST[i], font=("System", 20),
                                 variable=ck_val[i])
    ck_btn[i].place(x = 100, y = 150+50*i)

submit = tkinter.Button(text="확인", font=("System", 20), command=btn_check)
submit.place(x = 100, y = 350)
    
win.mainloop()
