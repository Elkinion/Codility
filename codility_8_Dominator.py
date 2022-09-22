# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:23:17 2022

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
        return(-1)
    n=len(A)
    times=0
    for i in A:
        if i==stack[-1]:
            times+=1
    if times>n/2:
        return(A.index(stack[-1]))
    else:
        return(-1)
    pass

A=[3,4,3,2,3,-1,3,3]
A=[]
A=[2, 1, 1, 3, 4]
solution(A)