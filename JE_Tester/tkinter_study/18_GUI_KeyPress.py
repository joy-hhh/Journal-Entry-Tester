import tkinter

key = ""

def key_down(e):
    global key
    key = e.keysym
    print("키 입력 : " + str(key))

def main_proc():
    label["text"] = key
    win.after(100, main_proc)
    
win = tkinter.Tk()
win.title("키 이벤트 발생하기")
win.bind("<KeyPress>", key_down)

#라벨 붙이기 - 키입력 출력 
label = tkinter.Label(text="키 입력전 ", font=("System", 30))
label.pack()
main_proc()
win.mainloop()




