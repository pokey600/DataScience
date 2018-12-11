import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
s = pd.Series([1,3,5,np.nan,6,8])
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
s1 = pd.Series([1,2,3,4,5,6], index=pd.date_range('20130102', periods=6))
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
df1.loc[dates[0]:dates[1],'E'] = 1
df1.dropna(how='any')
pd.read_excel('WHR2018Chapter2OnlineData.xls', 'Sheet1', index_col=None, na_values=['NA'])
df = pd.DataFrame(np.random.randn(10, 4))
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=['A', 'B', 'C', 'D'])
df = df.cumsum()
plt.figure(); df.plot(); plt.legend(loc='best')