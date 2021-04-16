import os
import xlsxwriter
import pandas as pd
folder = os.getcwd() + '\\data\\ch06\\'
csv_file = folder + "korea_rain.csv"

df = pd.read_csv(csv_file)

excel_file = folder + 'XlsxWriter_DF_01.xlsx'
excel_writer = pd.ExcelWriter(excel_file, engine='xlsxwriter')

df.to_excel(excel_writer, sheet_name = 'good')

excel_writer.save()
