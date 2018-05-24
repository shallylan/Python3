#!/usr/bin/env python3
import sys, csv

class Args:
    def __init__(self):
        l = sys.argv[1:]
        self.c = l[l.index('-c')+1]
        self.d = l[l.index('-d')+1]
        self.o = l[l.index('-o')+1]

args = Args()

class Config:
    def __init__(self):
        with open(args.c) as f:
            config = {'s': 0}
            for i in f.readlines():
                a, b = i.split('=')
                a, b = a.strip(), float(b)
                if b > 1:
                    config[a] = b
                else:
                    config['s'] += b
        self.con = config

config = Config().con

def cal(workno, salary):
    shebao = salary * config['s']
    if salary < config['JiShuL']:
        shebao = config['JiShuL'] * config['s']
    if salary > config['JiShuH']:
        shebao = config['JiShuH'] * config['s']
    cut = salary - shebao -3500
    if cut <=0:
        tax = 0
    elif cut<1500:
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
    else:
        tax = cut * 0.45 - 13505
    return [workno, salary, format(shebao, '.2f'),
        format(tax, '.2f'), format(salary-shebao-tax, '.2f')]

with open(args.d) as f:
    userdata = list(csv.reader(f))

with open(args.o, 'w') as f:
    for a, b in userdata:
        csv.writer(f).writerow(cal(a, int(b)))
