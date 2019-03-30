import os
import matplotlib.pyplot as plt
import pandas as pd

DATA_PATH = "datasets"
def Loaddata(path = DATA_PATH):
  xlsx_path = os.path.join(path, "KOSDAQ_TICKER.xlsx")
  return pd.read_excel(xlsx_path, header=0 ,index=1,dtype={'종목코드': str} )

df = Loaddata()
df.set_index('종목코드', inplace=True)

targetCodes = ['078130', '076080' , '073010','072770','023460','033560',  '039830','068330','001810']
targetdata = df.loc[targetCodes]
graphNo = 0

fig, axes = plt.subplots(nrows=3, ncols=3)
for x in range(9):
  targetdata.iloc[x].plot(ax=axes[x//3,x%3])

plt.show()