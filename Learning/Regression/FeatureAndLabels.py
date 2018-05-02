import pandas as pd
import quandl
import math

df = quandl.get("WIKI/GOOGL")

#print(df.head())

df = df[['Adj. Open','Adj. Close','Adj. High','Adj. Volume']]
df['High_Percent'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] * 100
df['Percent_Change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100

df = df[['Adj. Close','High_Percent','Percent_Change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01 * len(df)))

df['Label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

print(df.head())
