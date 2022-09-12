# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 20:35:14 2022

@author: Elkin Gutierrez
"""

def solution(A):
    n=0
    for i in A:
        n=n^i#Xor operator is all the trick, a^a=0 and the operation is abelian.
    return(n)
    pass


#another way to do it.
from functools import reduce

def sol(B):
    r = reduce((lambda x, y: x ^ y), B)
    return(r)

#list1 = [1, 2, 3,2,1]
#sol(list1)