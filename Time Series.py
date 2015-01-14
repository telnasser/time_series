import pandas as pd
import numpy as np 

df = pd.read_csv('LoanStats3b.csv', header=1, low_memory=False)

df.head()
df.columns

df['issue_d']

df['list_d_format'] = pd.to_datetime(df['issue_d']) 

print df['list_d_format']

dfts = df.set_index('list_d_format')

dfts
year_month_summary = dfts.groupby(lambda x : x.year*100+x.month).count()
year_month_summary

loan_count_summary = year_month_summary['issue_d']

loan_count_summary 

import statsmodels.api as sm


loan_count_summary.plot()


year_month_summary.plot()
