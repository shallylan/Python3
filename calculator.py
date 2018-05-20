#!/usr/bin/env python3
import sys
workno = sys.argv[1]
salary = sys.argv[2]

try:
	cut = sys.argv[2] * (1-0.165)-3500
	if cut <=0:
		tax = 0
		print("workno {},tax {:2f}".format(workno, tax)
	elif cut > 0:
		if cut<1500:
			tax = cut * 0.03 -0
		elif cut > 1500 and cut <= 4500:
			tax = cut * 0.1 - 105
		elif cut > 4500 and cut <= 9000:
			tax = cut * 0.2 - 555
		elif cut > 9000 and cut <= 350000:
			tax = cut * 0.25 - 1005
		elif cut > 35000 and cut <= 55000:
			tax = cut * 0.3 - 2755
		elif cut > 55000 and cut <=


except ValueError:
	print("Parameter Error")
