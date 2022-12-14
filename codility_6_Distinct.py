# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 12:01:29 2022

@author: Elkin Gutierrez
"""
"""
Write a function

def solution(A)

that, given an array A consisting of N integers, returns the number of distinct values in array A.

For example, given array A consisting of six elements such that:

 A[0] = 2    A[1] = 1    A[2] = 1
 A[3] = 2    A[4] = 3    A[5] = 1
the function should return 3, because there are 3 distinct values appearing in array A, namely 1, 2 and 3.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

## sort the array first and consecutive elements are the same if there are more than one of the same
def solution(A):
    A.sort()
    n=len(A)
    if n==0:
        return(0)
    count=1
    for i in range(1,n):
        if A[i]!=A[i-1]:
            count+=1
    return(count)
    pass
    pass