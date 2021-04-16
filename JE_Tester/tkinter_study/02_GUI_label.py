import tkinter

win = tkinter.Tk()
win.title("파이썬 GUI 프로그램 라벨 붙이기")
win.geometry("400x300")
#라벨을 붙이기
label = tkinter.Label(win, text="성공했다면 클릭하세요", font=("System", 15))
label.place(x=200, y=150)
win.mainloop()
