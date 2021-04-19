import pandas as pd
import os



df = pd.read_excel("c:/je/je.xlsx")
df.columns
acct = 'ACCTCD'
a =df.groupby(acct)
b = df.ACCTCD.unique()
b

Date_Format = {'20211231' : '%Y%m%d','2021-12-31': '%Y-%m-%d','2021/12/31': '%Y/%m/%d','12/31/2021':'%m/%d/%Y'}

combobox11 = 20211231
Date_Format[str(combobox11)]

ac = 'ACCTCD'
accode = '40401'
df1 = df.astype({ac: 'str'})
dfaccode = (df1[ac] == accode)
jeaccode = df1[dfaccode]
jenoaccode = jeaccode['JENO']
dfaccode = df1[['JENO', 'ACCTCD']]
jenomerge = pd.merge(jenoaccode, dfaccode, left_on='JENO', right_on='JENO', how='left')
accodegb = jenomerge.groupby("ACCTCD").count()
accodegb.to_excel(folder + 'B1test.xlsx')
lbl6.configure(text="Corr. Acc. Count : " + str(accodegb.shape[0] - 1))