# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:53:27 2022

@author: Elkin Gutierrez
"""

def solution(A, B, K):
    if A<K and A%K!=0:
        B=B-K
    else:    
        residual=A%K
        B=B-A-residual
    result=B//K
    return(result+1)


A,B,K=[101, 123456789, 10000]
A,B,K=[6, 11, 2]

solution(A, B, K)