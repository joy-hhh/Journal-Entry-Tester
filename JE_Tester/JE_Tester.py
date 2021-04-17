import pandas as pd
import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog

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
win.geometry("1000x800")
win.title("JE Tester by Joy 0.1.0, Copyright 2021. Joy. All rights reserved ")
win.option_add("*Font","NanumGothic 16")

frame_file = Frame(win, relief = solid, bd = 1)
frame_file.pack()

b0 = Button(win, text = "JE File Upload",command=readexcel)
b0.grid(row=0, column=0, sticky = N+E+W+S, padx =10)

sel_lab1 = Label(win, text = "Select ACCT Code")
sel_lab1.grid(row=1, column=0, sticky = W, padx =10)
ACCT = [str(i) for i in range(1,32)]
combobox1 = ttk.Combobox(win,height =5, state="readonly", values = ACCT)
combobox1.grid(row = 1, column = 1)
combobox1.set("Select ACCT Code")

sel_lab2 = Label(win, text = "Select JE No.")
sel_lab2.grid(row=2, column=0, sticky = W, padx =10)
JENO = [str(i) for i in range(1,32)]
combobox2 = ttk.Combobox(win,height =5, state="readonly", values = JENO)
combobox2.grid(row = 2, column = 1)
combobox2.set("Select JE No.")

sel_lab3 = Label(win, text = "Select JE Date")
sel_lab3.grid(row=3, column=0, sticky = W, padx =10)
JEDATE = [str(i) for i in range(1,32)]
combobox3 = ttk.Combobox(win,height =5, state="readonly", values = JEDATE)
combobox3.grid(row = 3, column = 1)
combobox3.set("Select JE Date")

sel_lab4 = Label(win, text = "Select Debit Record")
sel_lab4.grid(row=4, column=0, sticky = W, padx =10)
DR = [str(i) for i in range(1,32)]
combobox4 = ttk.Combobox(win,height =5, state="readonly", values = DR)
combobox4.grid(row = 4, column = 1)
combobox4.set("Select DR")

sel_lab5 = Label(win, text = "Select Credit Record")
sel_lab5.grid(row=5, column=0, sticky = W, padx =10)
CR = [str(i) for i in range(1,32)]
combobox5 = ttk.Combobox(win,height =5, state="readonly", values = CR)
combobox5.grid(row = 5, column = 1)
combobox5.set("Select CR")



b6 = Button(win, text = "TB(CY) File Upload",command=readexcel)  # command attach
b6.grid(row=0, column=3, sticky = N+E+W+S, padx =10)

ACCT_CYTB = [str(i) for i in range(1,32)]
combobox7 = ttk.Combobox(win,height =5, state="readonly", values = ACCT_CYTB)
combobox7.grid(row = 1, column = 3)
combobox7.set("Select ACCT Code")

ACCT_DRSUM = [str(i) for i in range(1,32)]
combobox8 = ttk.Combobox(win,height =5, state="readonly", values = ACCT_DRSUM)
combobox8.grid(row = 2, column = 3)
combobox8.set("Select DR")

ACCT_CRSUM = [str(i) for i in range(1,32)]
combobox9 = ttk.Combobox(win,height =5, state="readonly", values = ACCT_CRSUM)
combobox9.grid(row = 3, column = 3)
combobox9.set("Select CR")

b7 = Button(win, text = "TB(PY) File Upload",command=readexcel) # command attach
b7.grid(row=0, column=4, sticky = N+E+W+S, padx =10)

ACCT_PYTB = [str(i) for i in range(1,32)]
combobox11 = ttk.Combobox(win,height =5, state="readonly", values = ACCT_PYTB)
combobox11.grid(row = 1, column = 4)
combobox11.set("Select ACCT Code")

ACCT_DRSUM_PY = [str(i) for i in range(1,32)]
combobox12 = ttk.Combobox(win,height =5, state="readonly", values = ACCT_DRSUM_PY)
combobox12.grid(row = 2, column = 4)
combobox12.set("Select DR")

ACCT_CRSUM_PY = [str(i) for i in range(1,32)]
combobox13 = ttk.Combobox(win,height =5, state="readonly", values = ACCT_CRSUM_PY)
combobox13.grid(row = 3, column = 4)
combobox13.set("Select CR")





l2 = Label(win, text = "Beg date")
l3 = Label(win, text = "End date")
l4 = Label(win, text = "Date Format")
l5 = Label(win, text = "Column for NA Lines")
l6 = Label(win, text = "Account Code for B01")

l2.grid(row=11, column=0, sticky = E, padx =10)
l3.grid(row=12, column=0, sticky = E, padx =10)
l4.grid(row=13, column=0, sticky = E, padx =10)
l5.grid(row=14, column=0, sticky = E, padx =10)
l6.grid(row=15, column=0, sticky = E, padx =10)



lbl0 = Label(win, text ="JE file (Row, Col) : ? ")
lbl0.grid(row=0, column=1, sticky = N+E+W+S,  pady = 20)
e2=Entry(win)
e3=Entry(win)


e2.grid(row=11, column =1)
e2.insert(0, "2017-01-01")
e3.grid(row=12, column =1)
e3.insert(0, "2017-12-31")

# e4 replace to combobox
Date_Format = {'20211231' : '%Y%m%d','2021-12-31': '%Y-%m-%d','2021/12/31': '%Y/%m/%d','12/31/2021':'%m/%d/%Y'}
combobox13 = ttk.Combobox(win,height =5, state="readonly", values = list(Date_Format.keys()))
combobox13.grid(row = 13, column = 1)
combobox13.set("Select Date Format")

# e5 replace to combobox
NA_lines =  [str(i) for i in range(1,32)]
combobox14 = ttk.Combobox(win,height =5, state="readonly", values = NA_lines)
combobox14.grid(row = 14, column = 1)
combobox14.set("Select column for NA")


# e6 replace to combobox
ACCT_B01 =  [str(i) for i in range(1,32)]
combobox15 = ttk.Combobox(win,height =5, state="readonly", values = ACCT_B01)
combobox15.grid(row = 15, column = 1)
combobox15.set("Select column for B01")



b22 = Button(win, text = "A01(1)", command=A1_1)
b23 = Button(win, text = "A01(2)", command=A1_2)
b24 = Button(win, text = "A02", command=A2)
b25 = Button(win, text = "A03", command=A3)
b26 = Button(win, text = "B01", command=B1)
b50 = Button(win, text = "Save JE_Test File", command=B1)  # attach command

b22.grid(row=22,column =0, sticky = N+E+W+S)
b23.grid(row=23,column =0, sticky = N+E+W+S)
b24.grid(row=24,column =0, sticky = N+E+W+S)
b25.grid(row=25,column =0, sticky = N+E+W+S)
b26.grid(row=26,column =0, sticky = N+E+W+S)
b50.grid(row=50,column =0, sticky = N+E+W+S, columnspan =2)





lbl2 = Label(win, text ="Out of FY Row EA : ? ")
lbl2.grid(row=22, column=1, sticky = W)

lbl3 = Label(win, text ="NA EA : ? ")
lbl3.grid(row=23, column=1, sticky = W)

lbl4 = Label(win, text ="Amount Diff. EA : ? ")
lbl4.grid(row=24, column=1, sticky = W)

lbl5 = Label(win, text ="Je TB Diff. EA : ? ")
lbl5.grid(row=25, column=1, sticky = W)

lbl6 = Label(win, text ="Corr. ACCT Code EA : ? ")
lbl6.grid(row=26, column=1, sticky = W)


win.mainloop()

