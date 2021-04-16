import tkinter

def click_btn():
    txt1 = int(entry1.get())
    txt2 = int(entry2.get())
    txt3 = txt1+txt2
    button["text"] = txt3
    
win = tkinter.Tk()
win.title("엔트리(텍스트 입력 필드) 사용하기")
win.geometry("400x400")

#첫번째 입력
entry1 = tkinter.Entry(width=30)
entry1.place(x=20, y=20)

#두번째 입력
entry2 = tkinter.Entry(width=30)
entry2.place(x=20, y=40)

button = tkinter.Button(text="합 계산", command=click_btn)
button.place(x=20, y=70)
win.mainloop()
