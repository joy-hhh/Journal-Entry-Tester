
import pandas as pd


# 여러 개의 DataFrame 데이터를 하나의 엑셀 워크시트에 위치를 지정해 쓰는 예

df1 = pd.DataFrame({'제품ID': ['P1001', 'P1002', 'P1003', 'P1004'],
                    '판매가격': [5000,7000,8000,9000],
                    '판매량': [50,93,70,48]})
df2 = pd.DataFrame({'제품ID': ['P2001', 'P2002', 'P2003', 'P2004'],
                    '판매가격': [5200,7200,8200,9200],
                    '판매량': [51,94,72,58]})
df3 = pd.DataFrame({'제품ID': ['P3001', 'P3002', 'P3003', 'P3004'],
                    '판매가격': [5300,7300,8300,9300],
                    '판매량': [51,94,72,58]})
df4 = pd.DataFrame({'제품ID': ['P4001', 'P4002', 'P4003', 'P4004'],
                    '판매가격': [5500,7400,8500,9400],
                    '판매량': [53,96,76,78]})
import os
folder = os.getcwd() + '\\data\\ch05\\'
excel_file = folder + 'product_sales_in_one_worksheet.xlsx'
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

df1.to_excel(excel_writer)
df2.to_excel(excel_writer, startrow=0, startcol=5, index=False)
df3.to_excel(excel_writer, startrow=6, startcol=0,)
df4.to_excel(excel_writer, startrow=5, startcol=5, index=False, header=False)
excel_writer.save()

print("생성한 엑셀 파일 : ", excel_file)
