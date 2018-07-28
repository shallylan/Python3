import json, sys
import numpy as numpy
import pandas as pd

def analysis(file, user_id):
	data = pd.read_json(file)
	s = data[data['user_id']== user_id].minutes

	return s.count(), s.sum()

#print(analysis('user_study.json', 199071))
if __name__ == '__main__':
    user_id = int(sys.argv[1])
    print(analysis('user_study.json', user_id))
