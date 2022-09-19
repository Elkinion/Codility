# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:38:03 2022

@author: Elkin Gutierrez
"""

def solution(A):
    A.sort()
    n=len(A)
    if n<3:
        return(0)
    for i in range(n-2):
        if A[i]+A[i+1]>A[i+2]:
            return(1)
    return(0)
    pass