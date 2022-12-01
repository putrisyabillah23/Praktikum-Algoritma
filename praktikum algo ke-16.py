# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 22:01:19 2022

@author: putri
"""

def tukar(A, i, j):
    tempt = A[i]
    A[i]=A[j]
    A[j]=tempt

def BubbleSort(A, n):
    for i in range(n-1):
        if A[i] > A[i+1]:
            tukar(A, i, i+1)
        if n-1 > 1 :
            BubbleSort(A, n-1)

A = [2,23,45,3,7,1,21,56,6]
BubbleSort(A, len(A))
print("")
print(A)
            

            