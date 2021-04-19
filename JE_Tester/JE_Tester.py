import pandas as pd
import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

win =Tk()
win.geometry("1200x800")
win.title("JE Tester by Joy 0.1.0, Copyright 2021. Joy. All rights reserved ")
win.option_add("*Font","NanumGothic 16")


filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                      filetypes=(("XLSX files", "*.xlsx"),
                                                 ("All files", "*.*")))
folder = os.path.abspath(filename)
df = pd.read_excel(filename)

def readexcel():
    try:
        lbl0.configure(text="JE file (Row, Col) : " + str(df.shape))
    except Exception as err:
        msgbox.showerror("Error", err)

# %% A1 datetime

from datetime import datetime


def A1_1():
    try:
        start = str(e3.get())
        end = str(e4.get())
        date_format = Date_Format[str(combobox11.get())]
        df['date'] = pd.to_datetime(df[str(combobox5.get())], format=date_format)
        before = df['date'] < pd.to_datetime(start)
        after = df['date'] > pd.to_datetime(end)
        out = df[before | after]
        lbl2.configure(text="out of FY line Count : " + str(out.shape[0]))
    except Exception as err:
        msgbox.showerror("Error", err)

def A1_2():
    try:
        nullcol = str(e5.get())
        nulltemp = df[nullcol].isnull()
        nullrow = df.loc[(nulltemp)]
        lbl3.configure(text="NA Line Count : " + str(nullrow.shape[0]))
    except Exception as err:
        msgbox.showerror("Error", err)

# %% A2 account differ

def A2():
    try:
        cha = df.pivot_table(values=[str(combobox2.get())], index=[str(combobox4.get())], aggfunc='sum', margins=True)
        dae = df.pivot_table(values=[str(combobox3.get())], index=[str(combobox4.get())], aggfunc='sum', margins=True)
        test = pd.concat([cha, dae], axis=1)
        test['difference'] = test[str(combobox2.get())] - test[str(combobox3.get())]
        # difference Row groupby
        test.to_excel(folder + 'A2test.xlsx')
        A2_test = test.groupby("difference").count()
        lbl4.configure(text="Amount diff. Count : " + str(A2_test.shape[0] - 1))
    except Exception as err:
        msgbox.showerror("Error", err)


# %% B1 corr

def B1():
    try:
        accode = str(e6.get())
        df1 = df.astype({str(combobox1.get()): 'str'})
        dfaccode = (df1[str(combobox1.get())] == accode)
        jeaccode = df1[dfaccode]
        jenoaccode = jeaccode[str(combobox4.get())]
        dfaccode = df1[[str(combobox4.get()), str(combobox1.get())]]
        jenomerge = pd.merge(jenoaccode, dfaccode, left_on=str(combobox4.get()), right_on=str(combobox4.get()), how='left')
        accodegb = jenomerge.groupby(str(combobox1.get())).count()
        accodegb.to_excel(folder + 'B1test.xlsx')
        lbl6.configure(text="Corr. Acc. Count : " + str(accodegb.shape[0] - 1))
    except Exception as err:
        msgbox.showerror("Error", err)

# Title

Label(win, text = "Journal Entry Test Tool").pack(side = "top")


# Frame

frame_file = Frame(win, relief = "solid", bd = 1)
frame_file.pack(fill = "both", expand = True)

lbl0 = Label(frame_file, text ="JE file (Row, Col) : ? ")
lbl0.grid(row=1, column=1, sticky = N+E+W+S,  pady = 20)

lbl_file = Label(frame_file, text ="File Settings : ")
lbl_file.grid(row=0, column=0, sticky = W)

frame_test = Frame(win, relief = "solid", bd = 1)
frame_test.pack(fill = "both", expand = True)

lbl_test = Label(frame_test, text ="Test Section : ")
lbl_test.grid(row=10, column=0, sticky = W)


b0 = Button(frame_file, text = "JE File Check",command=readexcel)
b0.grid(row=1, column=0, sticky = N+E+W+S, padx =10)

sel_lab1 = Label(frame_file, text = "Select ACCT Code")
sel_lab1.grid(row=2, column=0, sticky = W, padx =10)
ACCT = list(df.columns)
combobox1 = ttk.Combobox(frame_file,height =5, state="readonly", values = ACCT)
combobox1.grid(row = 2, column = 1)
combobox1.set("Select ACCT Code")

sel_lab2 = Label(frame_file, text = "Select Debit Record")
sel_lab2.grid(row=3, column=0, sticky = W, padx =10)
DR = list(df.columns)
combobox2 = ttk.Combobox(frame_file,height =5, state="readonly", values = DR)
combobox2.grid(row = 3, column = 1)
combobox2.set("Select DR")

sel_lab3 = Label(frame_file, text = "Select Credit Record")
sel_lab3.grid(row=4, column=0, sticky = W, padx =10)
CR = list(df.columns)
combobox3 = ttk.Combobox(frame_file,height =5, state="readonly", values = CR)
combobox3.grid(row = 4, column = 1)
combobox3.set("Select CR")


sel_lab4 = Label(frame_file, text = "Select JE No.")
sel_lab4.grid(row=5, column=0, sticky = W, padx =10)
JENO = list(df.columns)
combobox4 = ttk.Combobox(frame_file,height =5, state="readonly", values = JENO)
combobox4.grid(row = 5, column = 1)
combobox4.set("Select JE No.")

sel_lab5 = Label(frame_file, text = "Select JE Date")
sel_lab5.grid(row=6, column=0, sticky = W, padx =10)
JEDATE = list(df.columns)
combobox5 = ttk.Combobox(frame_file,height =5, state="readonly", values = JEDATE)
combobox5.grid(row = 6, column = 1)
combobox5.set("Select JE Date")



# %% TB Upload for A3

def CYTB_upload():
    global CYTB_file
    global CYTB
    CYTB_file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("XLSX files", "*.xlsx"),
                                                      ("All files", "*.*")))
    CYTB = pd.read_excel(CYTB_file)

    ACCT_CYTB = list(CYTB.columns)
    combobox7 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_CYTB)
    combobox7.grid(row=2, column=3)
    combobox7.set("Select ACCT Code")

    ACCT_DRSUM = list(CYTB.columns)
    combobox8 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_DRSUM)
    combobox8.grid(row=3, column=3)
    combobox8.set("Select DR Sum")

    ACCT_CRSUM = list(CYTB.columns)
    combobox9 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_CRSUM)
    combobox9.grid(row=4, column=3)
    combobox9.set("Select CR Sum")


def PYTB_upload():
    global PYTB_file
    global PYTB
    PYTB_file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("XLSX files", "*.xlsx"),
                                                      ("All files", "*.*")))
    PYTB = pd.read_excel(PYTB_file)

    ACCT_PYTB = list(PYTB.columns)
    combobox24 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_PYTB)
    combobox24.grid(row=2, column=4)
    combobox24.set("Select ACCT Code")

    ACCT_DRSUM_PY = list(PYTB.columns)
    combobox34 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_DRSUM_PY)
    combobox34.grid(row=3, column=4)
    combobox34.set("Select DR")

    ACCT_CRSUM_PY = list(PYTB.columns)
    combobox44 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_CRSUM_PY)
    combobox44.grid(row=4, column=4)
    combobox44.set("Select CR")


# %% A3

def A3():
    try:
        acccha = df.pivot_table(values=["DR"], index=["ACCTCD"], aggfunc='sum', margins=True)
        accdae = df.pivot_table(values=["CR"], index=["ACCTCD"], aggfunc='sum', margins=True)
        acc = pd.concat([acccha, accdae], axis=1)
        acc['inc'] = acc["DR"] - acc["CR"]

        n = e_BSPL.get()
        TB1 = CYTB.iloc[:(n-1), ]
        TB2 = CYTB.iloc[(n-1):, ]
        TB3 = PYTB

        TB1['inc'] = TB1['DRSUM'] - TB1['CRSUM']
        TB2['CYinc'] = TB2['DRSUM'] - TB2['CRSUM']
        TB3['inc'] = TB3['DRSUM'] - TB3['CRSUM']

        CYFPTBnull = (TB1['ACCTCD'].isnull())
        CYFPTB_adj = TB1.loc[(~CYFPTBnull)]

        CYPLTBnull = (TB2['ACCTCD'].isnull())
        CYPLTB_adj = TB2.loc[(~CYPLTBnull)]

        TBFP = pd.merge(CYFPTB_adj, TB3, left_on='ACCTCD', right_on='ACCTCD', how='left')
        TBFP['CYinc'] = TBFP['inc_x'] - TBFP['inc_y']

        TBFPinc = TBFP[['ACCTCD', 'CYinc']]
        TBPLinc = CYPLTB_adj[['ACCTCD', 'CYinc']]

        TBinc = pd.concat([TBFPinc, TBPLinc], ignore_index=True)

        acc2 = pd.merge(TBinc, acc, left_on='ACCTCD', right_on='ACCTCD', how='left')
        acc2['A3'] = acc2['CYinc'] - acc2['inc']

        acc2.to_excel(folder + 'A3test.xlsx')

        A3_test = acc2.groupby("A3").count()
        lbl5.configure(text="JE TB diff. EA : " + str(A3_test.shape[0] - 1))
    except Exception as err:  # 예외 처리
        msgbox.showerror("Error", err)


b6 = Button(frame_file, text = "TB(CY) File Upload",command=CYTB_upload)  # command attach
b6.grid(row=1, column=3, sticky = N+E+W+S, padx =10)


e_BSPL = Entry(frame_file)
e_BSPL.insert(0,"F/P End Line Num.")
def clear(event):
    if e_BSPL.get() == "F/P End Line Num.":
        e_BSPL.delete(0,len(e_BSPL.get()))
e_BSPL.bind("<Button-1>", clear)
e_BSPL.grid(row=5, column =3)


b7 = Button(frame_file, text = "TB(PY) File Upload",command=PYTB_upload) # command attach
b7.grid(row=1, column=4, sticky = N+E+W+S, padx =10)



l2 = Label(frame_file, text = "Date Format")
l3 = Label(frame_file, text = "Beg date")
l4 = Label(frame_file, text = "End date")
l5 = Label(frame_file, text = "Column for NA Lines")
l6 = Label(frame_file, text = "Account Code for B01")

l2.grid(row=11, column=0, sticky = W, padx =10)

l3.grid(row=12, column=0, sticky = E, padx =10)
l4.grid(row=13, column=0, sticky = E, padx =10)
l5.grid(row=14, column=0, sticky = E, padx =10)
l6.grid(row=15, column=0, sticky = E, padx =10)



Date_Format = {'20211231' : '%Y%m%d','2021-12-31': '%Y-%m-%d','2021/12/31': '%Y/%m/%d','12/31/2021':'%m/%d/%Y'}
combobox11 = ttk.Combobox(frame_file,height =5, state="readonly", values = list(Date_Format.keys()))
combobox11.grid(row = 11, column = 1)
combobox11.set("Select Date Format")

e3=Entry(frame_file)
e3.grid(row=12, column =1)
e3.insert(0, "2017-01-01")

e4=Entry(frame_file)
e4.grid(row=13, column =1)
e4.insert(0, "2017-12-31")

# for A01(2) Test
NA_lines = list(df.columns)
combobox14 = ttk.Combobox(frame_file,height =5, state="readonly", values = NA_lines)
combobox14.grid(row = 14, column = 1)
combobox14.set("Column for A01(2)")

# e6 for B01 Test
e6=Entry(frame_file)
e6.grid(row=15, column =1)


b22 = Button(frame_test, text = "A01(1)", command=A1_1)
b23 = Button(frame_test, text = "A01(2)", command=A1_2)
b24 = Button(frame_test, text = "A02", command=A2)
b25 = Button(frame_test, text = "A03", command=A3)
b26 = Button(frame_test, text = "B01", command=B1)
b50 = Button(frame_test, text = "Save JE_Test File", command=B1)  # attach command

b22.grid(row=22,column =0, sticky = N+E+W+S)
b23.grid(row=23,column =0, sticky = N+E+W+S)
b24.grid(row=24,column =0, sticky = N+E+W+S)
b25.grid(row=25,column =0, sticky = N+E+W+S)

lbl2 = Label(frame_test, text ="Out of FY Row EA : ? ")
lbl2.grid(row=22, column=1, sticky = W)

lbl3 = Label(frame_test, text ="NA EA : ? ")
lbl3.grid(row=23, column=1, sticky = W)

lbl4 = Label(frame_test, text ="Amount Diff. EA : ? ")
lbl4.grid(row=24, column=1, sticky = W)

lbl5 = Label(frame_test, text ="Je TB Diff. EA : ? ")
lbl5.grid(row=25, column=1, sticky = W)

b26.grid(row=22,column =3, sticky = N+E+W+S)
lbl6 = Label(frame_test, text ="Corr. ACCT Code EA : ? ")
lbl6.grid(row=22, column=4, sticky = W)

b50.grid(row=50,column =0, sticky = N+E+W+S, columnspan =7)

win.mainloop()

