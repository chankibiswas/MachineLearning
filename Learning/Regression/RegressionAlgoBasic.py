import pandas as pd
import quandl

df = quandl.get("WIKI/GOOGL")

#print(df.head())

df = df[['Adj. Open','Adj. Close','Adj. High','Adj. Volume']]
df['High_Percent'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] * 100
df['Percent_Change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100

df = df[['Adj. Close','High_Percent','Percent_Change','Adj. Volume']]

print(df.head())
