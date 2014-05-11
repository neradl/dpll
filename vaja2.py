# -*- encoding: utf-8 -*-

from bool import *
from cnf import *
from dpll import *
from sudoku import *

f = open('newfile.txt', 'r+')
s=[]
i=1
for line in f:
    j=1
    for ch in line:
        if ch == "\n":
            break
        if ch != " ":
            s.append((i,j,int(ch)))
        j=j+1
    i=i+1

(a,b)=dpll(sudoku4(s))
for (k,v) in list(b.items()):
    if v == True:
        
            

