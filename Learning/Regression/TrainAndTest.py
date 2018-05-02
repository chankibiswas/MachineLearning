import pandas as pd
import quandl, math
import numpy as np
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = quandl.get("WIKI/GOOGL")

df = df[['Adj. Open','Adj. Close','Adj. High','Adj. Volume']]
df['High_Percent'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close'] * 100
df['Percent_Change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] * 100

df = df[['Adj. Close','High_Percent','Percent_Change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

forecast_out = int(math.ceil(0.01 * len(df)))

df['Label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop(['Label'], 1))
Y = np.array(df['Label'])

X = preprocessing.scale(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, Y_train)
accuracy = clf.score(X_test, Y_test)

print(accuracy)
