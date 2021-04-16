import pandas as pd
import os
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Progressbar
from tkinter import filedialog
import calendar
import threading


def readexcel():
    global filename
    global folder
    global df
    filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                          filetypes=(("XLSX files", "*.xlsx"),
                                          ("all files", "*.*")))
    folder = os.path.abspath(filename)
    df = pd.read_excel(filename)
    print(filename)
    lbl1.configure(text="Journal entry file (row, column) : " + str(df.shape))



# %% A1 datetime

from datetime import datetime


def A1_1():
    start = str(e2.get())
    end = str(e3.get())
    date_format = str(e4.get())
    df['date'] = pd.to_datetime(df['JEDATE'], format=date_format)
    before = df['date'] < pd.to_datetime(start)
    after = df['date'] > pd.to_datetime(end)
    out = df[before | after]
    lbl2.configure(text="out of FY line EA : " + str(out.shape[0]))


def A1_2():
    nullcol = str(e5.get())
    nulltemp = df[nullcol].isnull()
    nullrow = df.loc[(nulltemp)]
    lbl3.configure(text="NA number : " + str(nullrow.shape[0]))


# %% A2 account differ

def A2():
    cha = df.pivot_table(values=["DR"], index=["JENO"], aggfunc='sum', margins=True)
    dae = df.pivot_table(values=["CR"], index=["JENO"], aggfunc='sum', margins=True)
    test = pd.concat([cha, dae], axis=1)
    test['difference'] = test["DR"] - test["CR"]
    # difference Row groupby
    test.to_excel(folder + 'A2test.xlsx')
    A2_test = test.groupby("difference").count()
    lbl4.configure(text="Amount diff. EA : " + str(A2_test.shape[0] - 1))


# %% A3

def A3():
    acccha = df.pivot_table(values=["DR"], index=["ACCTCD"], aggfunc='sum', margins=True)
    accdae = df.pivot_table(values=["CR"], index=["ACCTCD"], aggfunc='sum', margins=True)
    acc = pd.concat([acccha, accdae], axis=1)
    acc['inc'] = acc["DR"] - acc["CR"]

    # A3 TB
    TB1 = pd.read_excel(folder + 'CYTBFP.xlsx')
    TB2 = pd.read_excel(folder + 'CYTBPL.xlsx')
    TB3 = pd.read_excel(folder + 'PYTB.xlsx')

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

# %% B1 corr


def B1():
    accode = str(e6.get())

    df1 = df.astype({'ACCTCD': 'str'})

    dfaccode = (df1['ACCTCD'] == accode)
    jeaccode = df1[dfaccode]
    jenoaccode = jeaccode['JENO']

    dfaccode = df1[['JENO', 'ACCTCD']]

    jenomerge = pd.merge(jenoaccode, dfaccode, left_on='JENO', right_on='JENO', how='left')
    accodegb = jenomerge.groupby("ACCTCD").count()

    accodegb.to_excel(folder + 'B1test.xlsx')

    lbl6.configure(text="Corr Acc EA : " + str(accodegb.shape[0] - 1))


win =Tk()
win.geometry("500x500")
win.title("JE Tester by Joy 0.1.0, Copyright 2021. Joy. All rights reserved ")
win.option_add("*Font","NanumGothic 16")


l0 = Label(win, text = "Input")

b0 = Button(win, text = "File Upload",command=readexcel)
l2 = Label(win, text = "Beg date")
l3 = Label(win, text = "End date")
l4 = Label(win, text = "Date Set")
l5 = Label(win, text = "NA Row")
l6 = Label(win, text = "Acc Code")

l0.grid(row=5, column=1)


b0.grid(row=6, column=0, sticky = W, padx =10)
l2.grid(row=7, column=0, sticky = W, padx =10)
l3.grid(row=8, column=0, sticky = W, padx =10)
l4.grid(row=9, column=0, sticky = W, padx =10)
l5.grid(row=10, column=0, sticky = W, padx =10)
l6.grid(row=11, column=0, sticky = W, padx =10)



lbl0 = Label(win, text ="JE file (Row, Col) : ? ")
lbl0.grid(row=6, column=1, sticky = W,  pady = 20)
e2=Entry(win)
e3=Entry(win)
e4=Entry(win)
e5=Entry(win)
e6=Entry(win)


e2.grid(row=7, column =1)
e3.grid(row=8, column =1)
e4.grid(row=9, column =1)
e5.grid(row=10, column =1)
e6.grid(row=11, column =1)



b1 = Button(win, text = "A01(1)",command=A1_1)
b2 = Button(win, text = "A01(2)",command=A1_2)
b3 = Button(win, text = "A02",command=A2)
b4 = Button(win, text = "A03",command=A3)
b5 = Button(win, text = "B01",command=B1)



b1.grid(row=22,column =0)
b2.grid(row=23,column =0)
b3.grid(row=24,column =0)
b4.grid(row=25,column =0)
b5.grid(row=26,column =0)




lbl2 = Label(win, text ="Out of FY Row EA : ? ")
lbl2.grid(row=22, column=1, sticky = W)

lbl3 = Label(win, text ="NA EA : ? ")
lbl3.grid(row=23, column=1, sticky = W)

lbl4 = Label(win, text ="Amount Diff. EA : ? ")
lbl4.grid(row=24, column=1, sticky = W)

lbl5 = Label(win, text ="Je TB Diff. EA : ? ")
lbl5.grid(row=25, column=1, sticky = W)

lbl6 = Label(win, text ="Corr EA : ? ")
lbl6.grid(row=26, column=1, sticky = W)


win.mainloop()

