import pandas as pd
import os


# df = pd.read_excel("c:/je/je.xlsx")
df = pd.read_excel("/home/joy/다운로드/je.xlsx")

acct = 'ACCTCD'
DR = str(DR)

acccha = df.pivot_table(values=[str(combobox2.get())], index=[str(combobox1.get())], aggfunc='sum', margins=True)
accdae = df.pivot_table(values=[str(combobox3.get())], index=[str(combobox1.get())], aggfunc='sum', margins=True)
acc = pd.concat([acccha, accdae], axis=1)
acc['inc'] = acc[str(combobox2.get())] - acc[str(combobox3.get())]

n = e_BSPL.get()
TB1 = CYTB.iloc[:(n - 1), ]
TB2 = CYTB.iloc[(n - 1):, ]
TB3 = PYTB

TB1['inc'] = TB1['DRSUM'] - TB1['CRSUM']
TB2['CYinc'] = TB2['DRSUM'] - TB2['CRSUM']
TB3['inc'] = TB3['DRSUM'] - TB3['CRSUM']

CYFPTBnull = (TB1[str(combobox23.get())].isnull())
CYFPTB_adj = TB1.loc[(~CYFPTBnull)]

CYPLTBnull = (TB2[str(combobox23.get())].isnull())
CYPLTB_adj = TB2.loc[(~CYPLTBnull)]

TBFP = pd.merge(CYFPTB_adj, TB3, left_on=str(combobox23.get()), right_on=str(combobox24.get()), how='left')
TBFP['CYinc'] = TBFP['inc_x'] - TBFP['inc_y']

TBFPinc = TBFP[[str(combobox23.get()), 'CYinc']]
TBPLinc = CYPLTB_adj[[str(combobox24.get()), 'CYinc']]

TBinc = pd.concat([TBFPinc, TBPLinc], ignore_index=True)

acc2 = pd.merge(TBinc, acc, left_on=str(combobox23.get()), right_on=str(combobox1.get()), how='left')
acc2['A3'] = acc2['CYinc'] - acc2['inc']

A3_test = acc2.groupby("A3").count()
lbl5.configure(text="JE - TB diff. Count : " + str(A3_test.shape[0] - 1))