import tkinter

win = tkinter.Tk()
win.title("캔버스 for구문을 이용한 도형 그리기")
#캔버스 바탕
canvas = tkinter.Canvas(width=600, height=600, bg="white")
canvas.pack()

#for구문을 이용해서 네모칸 채우기
for y in range(6):
    for x in range(6):    #0~5
        if(x==3):
            canvas.create_rectangle(x*100,y*100,x*100+100,y*100+100,fill="blue")
        else:
            canvas.create_rectangle(x*100,y*100,x*100+100,y*100+100,fill="red")

win.mainloop()
