import tkinter

win = tkinter.Tk()
win.title("캔버스 문자와 도형 그리기")
#캔버스 바탕
canvas = tkinter.Canvas(width=600, height=600, bg="white")

#문자열
canvas.create_text(200,80,text="캔버스 위에 문자열",fill="black", font=("System",25))

#라인입력
canvas.create_line(100,100,200,200,fill="red",width=3)
canvas.create_rectangle(200,200,300,300,fill="blue",width=3,outline="red")

canvas.pack()
win.mainloop()
