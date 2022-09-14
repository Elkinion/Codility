# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:07:48 2022

@author: Elkin Gutierrez
"""
def solution(X, Y, D):
    A=(Y-X)//D #we make the integer divission
    if (Y-X)%D==0: #we calculate de modulus to return the ceiling
        return(A)
    else:
        return(A+1)
    pass
