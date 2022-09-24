# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 15:00:40 2022

@author: Elkin Gutierrez
"""


def solution(N):
    A=int(N**(1/2))+1
    MaxFactor=0
    for i in range(1,A):
        if N%i==0:
            MaxFactor=max(MaxFactor,i)
    return(2*(MaxFactor+N//MaxFactor))
    pass
