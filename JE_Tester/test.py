from tkinter import filedialog
from tkinter import *

root = Tk()
root.title("Downloader")
root.geometry("540x300+100+100")
root.resizable(False, False)

root.dirName=filedialog.askdirectory()
#root.file = filedialog.askopenfile(initialdir='path', title='select file', filetypes=(('jpeg files', '*.jgp'), ('all files', '*.*')))
print (root.dirName);

root.mainloop()