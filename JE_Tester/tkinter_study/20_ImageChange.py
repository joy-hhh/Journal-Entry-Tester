import tkinter

def img_change():
    path = inputBox.get()
    img = tkinter.PhotoImage(file=path)
    label_Img.configure(image=img)
    label_Img.image=img
    
win = tkinter.Tk()
win.title("이미지 버튼별 표시.")
py_Img = tkinter.PhotoImage(file="img/01.png")

label_Img = tkinter.Label(win, text="이미지가 표시되는 부분입니다.", image=py_Img)
label_Img.pack()

inputBox = tkinter.Entry(win, text="이미지 이름을 입력하세요.")
inputBox.pack()

button = tkinter.Button(win, text="확인", command=img_change)
button.pack()

win.mainloop()
