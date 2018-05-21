#!/usr/bin/env python3
import sys
import calculator

list = sys.argv[1:]

try:
	for i in list:
		j = i.split(":")
		k=j[0]
		v=int(j[1])
		b=calculator.cal(k, v)
		print(b)
except ValueError:
	print("Parameter Error")

