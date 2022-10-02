# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 15:13:02 2022

@author: Elkin Gutierrez
"""
"""
A non-empty array A consisting of N integers is given.

A permutation is a sequence containing each element from 1 to N once, and only once.

For example, array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
is a permutation, but array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
is not a permutation, because value 2 is missing.

The goal is to check whether array A is a permutation.

Write a function:

class Solution { public int solution(int[] A); }

that, given an array A, returns 1 if array A is a permutation and 0 if it is not.

For example, given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
    A[3] = 2
the function should return 1.

Given array A such that:

    A[0] = 4
    A[1] = 1
    A[2] = 3
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [1..1,000,000,000].
"""

### count the ocurrences if one becomes higher than 1 return 0 if non then 1
def solution(A):
    n=len(A)
    count=[0]*(n+1)
    for i in range(n):
        if A[i]>n:
            return(0)
        if count[A[i]]==1:
            return(0)
        if count[A[i]]==0:
            count[A[i]]=1
            #print(count)    
    return(1)
    pass
