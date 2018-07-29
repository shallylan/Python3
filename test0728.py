import sys,json
import numpy as ny
import pandas as pd
import matplotlib.pyplot as plt

def analysis(file):
	data = pd.read_json(file)
	for i in data[data.columns[4]]:
		if i == 223917:
			break
		else:
			user_id = i
			s = data[data['user_id'] == user_id]['minutes']
			studytime = s.sum()


	fig = plt.figure()
	ax = fig.add_subplot(1, 1, 1)
	ax.set_title("StudyData")
	major_ticks = np.arange(0, 300000, 50000)
	minor_ticks = np.arange(0, 3000, 500)
	ax.set_xticks(major_ticks)
	ax.set_xticks(minor_ticks, minor=True)
	ax.set_yticks(major_ticks)
	ax.set_yticks(minor_ticks, minor=True)

	ax.xlable("User ID")
	ax.ylable("Study Time")

	ax.plot(user_id, studytime)

	return fig.show()