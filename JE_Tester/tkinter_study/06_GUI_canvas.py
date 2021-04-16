import tkinter
   
win = tkinter.Tk()
win.title("캔버스 테스트입니다.")
canvas = tkinter.Canvas(win, width=400, height=400, bg="blue")
canvas.pack()
py_img = tkinter.PhotoImage(file="python.png")
canvas.create_image(200,200,image=py_img)
win.mainloop()
