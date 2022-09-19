# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:01:29 2022

@author: Elkin Gutierrez
"""

def solution(A):
    A.sort()
    n=len(A)
    if n==0:
        return(0)
    count=1
    for i in range(1,n):
        if A[i]!=A[i-1]:
            count+=1
    return(count)
    pass
    pass