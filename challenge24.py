# -*- coding:utf-8 -*-

import pandas as pd
import numpy as np

def quarter_volume():
	data = pd.read_csv('apple.csv', header=0)
	t = pd.to_datetime(data['Date'])
	data1 = pd.DataFrame(data=data.values, columns=data.columns, index=t)
	data2 = data1.drop('Date', axis=1)
	a = data2.resample('Q').sum()
	b = a.sort_values(by='Volume', ascending=False).head()
	#c = b.iloc[1]
	second_volume = b['Volume']

	return second_volume

quarter_volume()