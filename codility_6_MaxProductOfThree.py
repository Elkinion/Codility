# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 14:01:24 2022

@author: Elkin Gutierrez
"""

    A.sort()
    n=len(A)
    B=[A[0],A[1],A[n-3],A[n-2],A[n-1]]
    result=max(B[0]*B[1]*B[4], B[4]*B[3]*B[2])
    return(result)
    pass
