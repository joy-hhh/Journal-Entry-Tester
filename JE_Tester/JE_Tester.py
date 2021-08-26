import pandas as pd
import xlsxwriter
import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
from datetime import datetime

win =Tk()
win.geometry("1200x800")
win.title("JE Tester by Joy 0.1.0, Copyright 2021. Joy. All rights reserved ")
win.option_add("*Font","NanumGothic 16")


filename = filedialog.askopenfilename(initialdir="/", title="Select file",
                                      filetypes=(("XLSX files", "*.xlsx"),
                                                 ("All files", "*.*")))
df = pd.read_excel(filename)

def readexcel():
    try:
        lbl0.configure(text="JE file (Row, Col) : " + str(df.shape))
    except Exception as err:
        msgbox.showerror("Error", err)


def Save_File():
    try:
        JE_Test = [' ',
                   'Journal Entry test',
                   ' ',
                   ' ',
                   '회사명',
                   '작성일자',
                   '작성자',
                   '검토자',
                   ' ',
                   ' ',
                   ' ',
                   'Step 1.    테스트 개요 및 목적 ',
                   ' ',
                   '재무제표에 대한 회계감사의 일환으로 감사대상기간 동안 발생한 모든 전표 데이터에 대한 무결성 및 비경상적인 거래가 존재하는지를 검증',
                   ' ',
                   '(1) 계정명(FSLI)  :    전체 계정',
                   '(2) 기준일 (Coverage date)  :    ' + str(e4.get()),
                   '(3) 테스트되는 경영자의 주장 (Assertion)  :    완전성 (C),정확성 (A),기간귀속구분 (CO),실재성 (E/O),권리 (R),공시(PD),평가(V)',
                   ' ',
                   'Step 2.    Test 대상 모집단',
                   ' ',
                   '(1) 모집단 총 행의 수와 열의 수  :  (행 , 열) = ' + str(df.shape),
                   '(2) 모집단의 완전성 확인  :  Step 5. Test 결과의 A1, A2, A3 참조',
                   ' ',
                   'Step 3.    오류의 정의',
                   ' ',
                   '재무보고 프로세스 관련, 부적절하거나 비경상적인 분개 및 수정사항',
                   ' ',
                   'Step 4.    Test 방법',
                   ' ',
                   'A01 . Data Integrity 검증 - 데이터 유효성을 검증하고, record에 대한 이해를 위한 절차',
                   '전표 데이터의 회계기간이 당해년도에 포함되는지 여부 검토',
                   '전표 주요 필드값의 누락 여부 검토를 통한 data integrity 검토',
                   ' ',
                   'A02. 전표번호 별 차대변 일치검증',
                   '전표번호 별 차변금액과 대변금액이 일치하는지 확인하여 전표 데이터의 완전성을 검토',
                   '차변금액과 대변금액이 일치하지 않을 경우 해당 전표를 추출하여 회사 측과 확인',
                   ' ',
                   'A03. 시산표 Reconciliation 검증(Trial Balance Rollforward Test)',
                   '기초 F/S잔액에 수령한 모든 전표의 계정과목 별 합계금액을 반영하여 도출한 기말 F/S 잔액과 회사 제시 F/S와의 일치 여부 검토',
                   ' ',
                   'B01. 매출의 상대계정분석(매출과 연관성이 낮은 계정이 포함된 비정상적인 거래)',
                   '매출에 대한 상대계정분석 결과 비정상적으로 처리된 회계처리가 있는지 검토하고 해당 전표 중 특정 금액 이상인 건을 추출하여 검토',
                   ' ',
                   'Step 5.    Test 결과',
                   ' ',
                   'A01 (1) :    회계기간에 속하지 않는 날짜열의 갯수를 ' + str(out.shape[0]) + '개로 확인 하였음 ',
                   'A01 (2) :    ' + str(combobox14.get())+' 열의 결측값 갯수가 ' + str(nullrow.shape[0]) + '개로 확인 하였음',
                   'A02     :    전표번호별 차변 금액의 합계와 대변 금액의 합계가 차이 나는 열이 ' + str(A2_test.shape[0] - 1) + '개로 확인 하였음 - A2test Sheet 참조 ',
                   'A03     :    전표에서의 각 계정코드별 금액 합계가 시산표 계정코드별 금액과 차이나는 항목이' + str(A3_test.shape[0] - 1) + '개로 확인 하였음 -  A3test Sheet 참조 ',
                   'B01     :    ' + str(e6.get())+ ' 계정코드에 대하여 전표에 전기된 모든 상대계정코드의 갯수가 ' + str(accodegb.shape[0] - 1) + '개로 확인 하였음 - B1test Sheet 참조',
                   ' ',
                   ' ',
                   'JE Test에 대한 추가 기술 >> ']

        file_path = filedialog.askdirectory()

        excel_file = file_path + '/Journal_Entry_Test.xlsx'
        workbook = xlsxwriter.Workbook(excel_file)
        worksheet = workbook.add_worksheet('JE_Test_Summary')
        for row_num, value in enumerate(JE_Test):
            worksheet.write(row_num, 1, value)
        cell_format1 = workbook.add_format()
        cell_format1.set_bottom(5)
        for i in range(5, 9):
            worksheet.write(f'C{i}', " ", cell_format1)
        worksheet.set_column(1, 2, 25)
        workbook.close()

        excel_writer = pd.ExcelWriter(file_path + '/Journal_Entry_Details.xlsx', engine='xlsxwriter')
        test.to_excel(excel_writer, sheet_name='A2test')
        acc2.to_excel(excel_writer, sheet_name='A3test')
        accodegb.to_excel(excel_writer, sheet_name='B1test')
        excel_writer.save()

        msgbox.showinfo("Save complete", "Journal_Entry_Test.xlsx, Journal_Entry_Details.xlsx")

    except Exception as err:
        msgbox.showerror("Error", err)


def A1_1():
    global out
    try:
        start = str(e3.get())
        end = str(e4.get())
        date_format = Date_Format[str(combobox11.get())]
        df['date'] = pd.to_datetime(df[str(combobox5.get())], format=date_format)
        before = df['date'] < pd.to_datetime(start)
        after = df['date'] > pd.to_datetime(end)
        out = df[before | after]
        lbl2.configure(text="회계기간 외의 행 갯수 : " + str(out.shape[0]))
    except Exception as err:
        msgbox.showerror("Error", err)

def A1_2():
    global nullrow
    try:
        nullcol = str(combobox14.get())
        nulltemp = df[nullcol].isnull()
        nullrow = df.loc[(nulltemp)]
        lbl3.configure(text="NA Lines : " + str(nullrow.shape[0]))
    except Exception as err:
        msgbox.showerror("Error", err)

# %% A2 account differ

def A2():
    global test
    global A2_test
    try:
        cha = df.pivot_table(values=[str(combobox2.get())], index=[str(combobox4.get())], aggfunc='sum', margins=True)
        dae = df.pivot_table(values=[str(combobox3.get())], index=[str(combobox4.get())], aggfunc='sum', margins=True)
        test = pd.concat([cha, dae], axis=1)
        test['difference'] = test[str(combobox2.get())] - test[str(combobox3.get())]
        # difference Row groupby
        A2_test = test.groupby("difference").count()
        lbl4.configure(text="금액이 차이나는 행 갯수 : " + str(A2_test.shape[0] - 1))
    except Exception as err:
        msgbox.showerror("Error", err)


# %% B1 corr

def B1():
    global accodegb
    try:
        accode = str(e6.get())
        df1 = df.astype({str(combobox1.get()): 'str'})
        dfaccode = (df1[str(combobox1.get())] == accode)
        jeaccode = df1[dfaccode]
        jenoaccode = jeaccode[str(combobox4.get())]
        dfaccode = df1[[str(combobox4.get()), str(combobox1.get())]]
        jenomerge = pd.merge(jenoaccode, dfaccode, left_on=str(combobox4.get()), right_on=str(combobox4.get()), how='left')
        accodegb = jenomerge.groupby(str(combobox1.get())).count()
        lbl6.configure(text="상대계정 갯수 : " + str(accodegb.shape[0] - 1))
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
    global combobox23
    global combobox33
    global combobox43
    CYTB_file = filedialog.askopenfilename(initialdir="/", title="Select file",
                                           filetypes=(("XLSX files", "*.xlsx"),
                                                      ("All files", "*.*")))
    CYTB = pd.read_excel(CYTB_file)

    ACCT_CYTB = list(CYTB.columns)
    combobox23 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_CYTB)
    combobox23.grid(row=2, column=3)
    combobox23.set("Select ACCT Code")

    ACCT_DRSUM = list(CYTB.columns)
    combobox33 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_DRSUM)
    combobox33.grid(row=3, column=3)
    combobox33.set("Select DR Sum")

    ACCT_CRSUM = list(CYTB.columns)
    combobox43 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_CRSUM)
    combobox43.grid(row=4, column=3)
    combobox43.set("Select CR Sum")


def PYTB_upload():
    global PYTB_file
    global PYTB
    global combobox24
    global combobox34
    global combobox44
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
    combobox34.set("Select DR Sum")

    ACCT_CRSUM_PY = list(PYTB.columns)
    combobox44 = ttk.Combobox(frame_file, height=5, state="readonly", values=ACCT_CRSUM_PY)
    combobox44.grid(row=4, column=4)
    combobox44.set("Select CR Sum")


# %% A3

def A3():
    global acc2
    global A3_test
    try:
        acccha = df.pivot_table(values=[str(combobox2.get())], index=[str(combobox1.get())], aggfunc='sum', margins=True)
        accdae = df.pivot_table(values=[str(combobox3.get())], index=[str(combobox1.get())], aggfunc='sum', margins=True)
        acc = pd.concat([acccha, accdae], axis=1)
        acc['inc'] = acc[str(combobox2.get())] - acc[str(combobox3.get())]

        n = int(e_BSPL.get())
        TB1 = CYTB.iloc[:n, ]
        TB2 = CYTB.iloc[n:, ]
        TB3 = PYTB

        TB1 = TB1.copy()
        TB2 = TB2.copy()

        TB1.loc[:,'inc'] = TB1.loc[:,str(combobox33.get())] - TB1.loc[:,str(combobox43.get())]
        TB2.loc[:,'TB_inc'] = TB2.loc[:,str(combobox33.get())] - TB2.loc[:,str(combobox43.get())]
        TB3.loc[:,'inc'] = TB3.loc[:,str(combobox34.get())] - TB3.loc[:,str(combobox44.get())]

        CYFPTBnull = (TB1[str(combobox23.get())].isnull())
        CYFPTB_adj = TB1.loc[(~CYFPTBnull)]

        CYPLTBnull = (TB2[str(combobox23.get())].isnull())
        CYPLTB_adj = TB2.loc[(~CYPLTBnull)]

        TBFP = pd.merge(CYFPTB_adj, TB3, left_on=str(combobox23.get()), right_on=str(combobox24.get()), how='left')
        TBFP['TB_inc'] = TBFP['inc_x'] - TBFP['inc_y']

        TBFPinc = TBFP[[str(combobox23.get()), 'TB_inc']]
        TBPLinc = CYPLTB_adj[[str(combobox24.get()), 'TB_inc']]

        TBinc = pd.concat([TBFPinc, TBPLinc], ignore_index=True)

        acc2 = pd.merge(TBinc, acc, left_on=str(combobox23.get()), right_on=str(combobox1.get()), how='left')
        acc2['A3'] = acc2['TB_inc'] - acc2['inc']

        A3_test = acc2.groupby("A3").count()
        lbl5.configure(text="전표와 시산표가 차이나는 행 갯수 : " + str(A3_test.shape[0] - 1))
    except Exception as err:
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
e3.insert(0, "2021-01-01")

e4=Entry(frame_file)
e4.grid(row=13, column =1)
e4.insert(0, "2021-12-31")

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
b50 = Button(frame_test, text = "Save JE_Test File", command=Save_File)

b22.grid(row=22,column =0, sticky = N+E+W+S)
b23.grid(row=23,column =0, sticky = N+E+W+S)
b24.grid(row=24,column =0, sticky = N+E+W+S)
b25.grid(row=25,column =0, sticky = N+E+W+S)

lbl2 = Label(frame_test, text ="회계기간 외의 행 갯수 : ? ")
lbl2.grid(row=22, column=1, sticky = W)

lbl3 = Label(frame_test, text ="NA Lines : ? ")
lbl3.grid(row=23, column=1, sticky = W)

lbl4 = Label(frame_test, text ="금액이 차이나는 행 갯수 : ? ")
lbl4.grid(row=24, column=1, sticky = W)

lbl5 = Label(frame_test, text ="전표와 시산표가 차이나는 행 갯수 : ? ")
lbl5.grid(row=25, column=1, sticky = W)

b26.grid(row=22,column =3, sticky = N+E+W+S)
lbl6 = Label(frame_test, text ="상대계정 갯수 : ? ")
lbl6.grid(row=22, column=4, sticky = W)

b50.grid(row=50,column =0, sticky = N+E+W+S, columnspan =7)

win.mainloop()

