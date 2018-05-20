#!/usr/bin/env python3
import sys

try:
	list = sys.argv[1:]
        
	for i in list:
		j = i.split(":")
		workno = int(j[0])
		salary = int(i[1])

def cal(salary,workno):

	cut = salary * (1-0.165)-3500
	if cut <=0:
		tax = 0
		a=print("workno {} tax {:2f}".format(workno, tax))
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
		elif cut > 55000 and cut <= 80000:
			tax = cut * 0.35 - 5505
		elif cut > 80000:
			tax = cut * 0.45
		else:
			pass
	else:
		pass
	a=print("workno {} tax {:2f}".format(workno, tax)
return a

except ValueError:
	print("Peremeter Error")
