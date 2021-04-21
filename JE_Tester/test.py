import pandas as pd
import openpyxl
import xlsxwriter
import os
import tkinter.ttk as ttk
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox as msgbox
from datetime import datetime


df = pd.read_excel("c:/je/je.xlsx")
# df = pd.read_excel("/home/joy/다운로드/je.xlsx")

date = '2021-12-31'
PM = 1000000

A11 = '하나'
A12 = '둘'
A2 = '셋'
A3 = '400'
B1 = '500'


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
           '(1) 계정명(FSLI)    전체 계정',
           '(2) 기준일 (Coverage date) 	' + date,
           '(3) 테스트되는 경영자의 주장 (Assertion) : 완전성 (C),정확성 (A),기간귀속구분 (CO),실재성 (E/O),권리 (R),공시(PD),평가(V)',
           ' ',
           'Step 2.    Test 대상 모집단',
           ' ',
           '(1) 모집단 총 행의 수와 열의 수 : (행 , 열) = ' + str(df.shape),
           '(2) 모집단의 완전성 확인	Step 5. Test 결과의 A1, A2, A3 참조',
           ' ',
           'Step 3.    오류의 정의',
           ' ',
           '재무보고 프로세스 관련, 부적절하거나 비경상적인 분개 및 수정사항',
           ' ',
           'Step 4.    Test 방법',
           ' ',
           'A01 : Data Integrity 검증 - 데이터 유효성을 검증하고, record에 대한 이해를 위한 절차',
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
           'A01 (1) : 회계기간에 속하지 않는 날짜열의 갯수를 ' + A11 + '개로 확인 하였음 ',
           'A01 (2) : '+'~~ 열의 결측값 갯수가 ' + A12 + '개로 확인 하였음',
           'A02     : 전표번호별 차변 금액의 합계와 대변 금액의 합계가 차이 나는 열이 ' + A2 +'개로 확인 하였음 - A2test Sheet 참조 ',
           'A03     : 전표에서의 각 계정코드별 금액 합계가 시산표 계정코드별 금액과 차이나는 항목이' + A3 +'개로 확인 하였음 -  A3test Sheet 참조 ',
           'B01     : '+'~~계정코드에 대하여 전표에 전기된 모든 상대계정코드의 갯수가 ' + B1+'개로 확인 하였음 - B1test Sheet 참조']



folder = ("c:/je/")
excel_file = folder + 'Journal_Entry_Test.xlsx'

workbook = xlsxwriter.Workbook(excel_file)
worksheet = workbook.add_worksheet('JE_Test_Summary')
for row_num, value in enumerate(JE_Test):
    worksheet.write(row_num , 1, value)
cell_format1 = workbook.add_format()
cell_format1.set_bottom(5)
for i in range(2,6):
    worksheet.write(f'C{i}', " ", cell_format1)
worksheet.set_column(1,2, 25)

test = pd.DataFrame({'a':['100','200','300']})
acc2 = pd.DataFrame({'b':['200','300','400']})
accodegb = pd.DataFrame({'c':['300','400',500]})

excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')
test.to_excel(excel_writer, sheet_name='A2test')
acc2.to_excel(excel_writer, sheet_name='A3test')
accodegb.to_excel(excel_writer, sheet_name='B1test')
excel_writer.save()

workbook.close()
