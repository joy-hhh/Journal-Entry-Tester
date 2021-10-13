import pandas as pd
df = pd.read_excel('c:/je/JE test 2/je_test_2.xlsx', dtype=str)
df['Converted Debit'] = pd.to_numeric(df['Converted Debit'])
df['Converted Credit'] = pd.to_numeric(df['Converted Credit'])
df.dtypes


CYTB = pd.read_excel('c:/je/JE test 2/CYTB_2.xlsx', dtype=str)

CYTB[str('차변금액')] = pd.to_numeric(CYTB[str('차변금액')])
CYTB[str('대변금액')] = pd.to_numeric(CYTB[str('대변금액')])
CYTB.dtypes


PYTB = pd.read_excel('c:/je/JE test 2/PYTB_2.xlsx', dtype=str)

PYTB[str('차변금액')] = pd.to_numeric(PYTB[str('차변금액')])
PYTB[str('대변금액')] = pd.to_numeric(PYTB[str('대변금액')])
PYTB.dtypes


accode = str(4910263201)
df1 = df.astype({str('Account No.'): 'str'})
dfaccode = df1['Account No.'] == accode
jeaccode = df1[dfaccode]

str(dfaccode)
df.to_excel('df.xlsx')
df1.to_excel('df1.xlsx')

df1.dtypes
type(accode)



acccha = df.pivot_table(values=str('Converted Debit'), index='Account No.', aggfunc='sum', margins=True)
accdae = df.pivot_table(values=str('Converted Credit'), index=str('Account No.'), aggfunc='sum', margins=True)
acc = pd.concat([acccha, accdae], axis=1)
acc['inc'] = acc[str('Converted Debit')] - acc[str('Converted Credit')]

n = 130
TB1 = CYTB.iloc[:n, ]
TB2 = CYTB.iloc[n:, ]
TB3 = PYTB

TB1 = TB1.copy()
TB2 = TB2.copy()

TB1.loc[:, 'inc'] = TB1.loc[:, str('차변금액')] - TB1.loc[:, str('대변금액')]
TB2.loc[:, 'TB_inc'] = TB2.loc[:, str('차변금액')] - TB2.loc[:, str('대변금액')]
TB3.loc[:, 'inc'] = TB3.loc[:, str('차변금액')] - TB3.loc[:, str('대변금액')]


CYFPTBnull = (TB1[str('Account')].isnull())
CYFPTB_adj = TB1.loc[(~CYFPTBnull)]

CYPLTBnull = (TB2[str('Account')].isnull())
CYPLTB_adj = TB2.loc[(~CYPLTBnull)]

TBFP = pd.merge(CYFPTB_adj, TB3, left_on=str('Account'), right_on=str('Account'), how='left')
TBFP['TB_inc'] = TBFP['inc_x'] - TBFP['inc_y']

TBFPinc = TBFP[[str('Account'), 'TB_inc']]
TBPLinc = CYPLTB_adj[[str('Account'), 'TB_inc']]

TBinc = pd.concat([TBFPinc, TBPLinc], ignore_index=True)

acc2 = pd.merge(TBinc, acc, left_on=str('Account'), right_on=str('Account No.'), how='left')
acc2['A3'] = acc2['TB_inc'] - acc2['inc']

A3_test = acc2.groupby("A3").count()
lbl5.configure(text="전표와 시산표가 차이나는 행 갯수 : " + str(A3_test.shape[0] - 1))