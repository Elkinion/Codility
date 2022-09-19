# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:34:54 2022

@author: Elkin Gutierrez
"""


def solution(S):
    stack = []
    keys = {"]":"[", "}":"{", ")": "("}
    topush = ["[", "{", "("]
    N=len(S)
    for i in range(0,N):
        if S[i] in topush:
            stack.append(S[i])
        elif keys[S[i]]!=stack.pop():
            return(0)
    if len(stack)==0:
        return(1)
    else:
        return(0)
    pass