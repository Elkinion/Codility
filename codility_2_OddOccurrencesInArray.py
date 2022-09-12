# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:35:14 2022

@author: Elkin Gutierrez
"""

def solution(A):
    n=0
    for i in A:
        n=n^i
    return(n)
    pass