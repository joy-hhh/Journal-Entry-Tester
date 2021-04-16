import tkinter

def click_button():
    button["text"] = "클릭했습니다."
    
    
win = tkinter.Tk()
win.title("파이썬 GUI 프로그램 버튼")
win.geometry("400x300")
#라벨을 붙이기
label = tkinter.Label(win, text="성공했다면 클릭하세요", font=("System", 20))
label.place(x=100, y=100)
#버튼을 붙이기
button = tkinter.Button(win, text="클릭하세요.", font=("System", 20), command=click_button)
button.place(x=100, y=150)
win.mainloop()
