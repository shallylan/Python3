import json
import numpy as numpy
import pandas as pd

def analysis(file，user_id):
	import pandas as pd
	data = pd.read_json(file, typ='frame')
	s = data[data['user_id']== user_id]

	return s.count(), s.sum()

print(analysis('user_study.json', 199071))
