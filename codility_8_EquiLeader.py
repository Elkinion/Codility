# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:19:22 2022

@author: Elkin Gutierrez
"""

def solution(A):
    stack=[]
    for i in A:
        if len(stack)==0:
            stack.append(i)
        elif stack[-1]==i:
            stack.append(i)
        else:
            stack.pop()
        #print(stack)
    if len(stack)==0:
        return(0)
    n=len(A)
    times=0
    dom=stack[-1]
    for i in A:
        if i==dom:
            times+=1
    #print(times)
    equi=0
    conteo=0
    for i in range(n):
        if dom==A[i]:
            conteo+=1
        if conteo>(i+1)/2 and (times-conteo)>(n-i-1)/2:
            equi+=1
        #print(conteo,(i+1)/2, (times-conteo),(n-i-1)/2)
    return(equi)
    pass


A=[4,3,4,4,4,2]
solution(A)