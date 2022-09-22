# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:48:27 2022

@author: Elkin Gutierrez
"""

def solution(S):
    n=len(S)
    stack=[]
    
    for i in range(n):
        if S[i]=='(':
            stack.append(S[i])
        else:
            if len(stack)==0:
                return(0)
            elif stack[-1]=='(':
                stack.pop()
    if len(stack)==0:
        return(1)
    else:
        return(0)
        