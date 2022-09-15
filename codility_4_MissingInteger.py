# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 22:05:10 2022

@author: Elkin Gutierrez
"""
"""
This is a demo task.

Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].
"""

def solution(A):
    n=len(A)
    pigeon=[0]*(n+1)
    for i in range(n):
        if A[i]<=0:
            next
        else:
            pigeon[A[i]-1]=1
        #print(pigeon)
    for i in range(n+1):
        if pigeon[i]==0:
            return(i+1)
    pass
        
A = [1, 3, 6, 4, 1, 2]
 
solution(A)