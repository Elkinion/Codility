# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:13:02 2022

@author: Elkin Gutierrez
"""

def solution(A):
    n=len(A)
    count=[0]*(n+1)
    for i in range(n):
        if A[i]>n:
            return(0)
        if count[A[i]]==1:
            return(0)
        if count[A[i]]==0:
            count[A[i]]=1
            #print(count)    
    return(1)
    pass
