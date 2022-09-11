# -*- coding: utf-8 -*-
"""
Created on Wed Sep  7 16:50:13 2022

@author: Elkin Gutierrez
"""

def solution(n):
    result=0
    count=0
    while n%2==0:
        n=n//2
    while n>1:
        if n%2==1:
            n=n//2
            count=0
        else:
            n=n//2
            count+=1
        result=max(result,count)
    
    return(result)

    pass
