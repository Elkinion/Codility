# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 16:24:36 2022

@author: Elkin Gutierrez
"""
"""
We draw N discs on a plane. The discs are numbered from 0 to N − 1. An array A of N non-negative integers, specifying the radiuses of the discs, is given. The J-th disc is drawn with its center at (J, 0) and radius A[J].

We say that the J-th disc and K-th disc intersect if J ≠ K and the J-th and K-th discs have at least one common point (assuming that the discs contain their borders).

The figure below shows discs drawn for N = 6 and A as follows:

  A[0] = 1
  A[1] = 5
  A[2] = 2
  A[3] = 1
  A[4] = 4
  A[5] = 0


There are eleven (unordered) pairs of discs that intersect, namely:

discs 1 and 4 intersect, and both intersect with all the other discs;
disc 2 also intersects with discs 0 and 3.
Write a function:

def solution(A)

that, given an array A describing N discs as explained above, returns the number of (unordered) pairs of intersecting discs. The function should return −1 if the number of intersecting pairs exceeds 10,000,000.

Given array A shown above, the function should return 11, as explained above.

Write an efficient algorithm for the following assumptions:
"""
def solution(A):
    n=len(A)
    L=[0]*n
    R=[0]*n
    for i in range(n):
        L[i]=i-A[i]
        R[i]=i+A[i]
    L.sort()
    R.sort()
    counter=0
    posL=0
    for posR in range(0,n):
        counter+=1
        if posL==n:
            break
        while L[posL]<R[posR]:
            print(L[posL], R[posR])
            posL+=1
            counter+=1
            if posL==n:
                break
    return(counter-1)
        
A=[1,5,2,1,4,0]

solution(A)



