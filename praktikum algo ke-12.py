# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 20:18:13 2022

@author: putri
"""

def pangkat(x,y):
    if y == 0:
        return 1
    else :
        return x * pangkat(x,y-1)

x = int(input("masukan angka :"))
y = int(input("masukan pangkatnya :"))

print("%d hasilnya adalah %d = %d" %(x,y, pangkat(x,y)))