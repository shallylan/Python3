#!/usr/bin/env python3
import sys
import calculator.cal

list = sys.argv[1:]

try:

	for i in list:
		j = i.split(":")
		k=j[0]
		v=int(j[1])
		cal(k, v)

except ValueError:
	print("Parameter Error")

