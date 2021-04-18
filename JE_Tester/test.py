import pandas as pd
import os

os.getcwd()

df = pd.read_excel("/home/joy/다운로드/Others 정리.xlsx")
df_col = list(df.columns)
df.shape
n = 5
FP = df.iloc[:n,]
IS = df.iloc[n:,]