# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 21:41:29 2022

@author: Elkin Gutierrez
"""
"""
A non-empty array A consisting of N integers is given.

A triplet (X, Y, Z), such that 0 ≤ X < Y < Z < N, is called a double slice.

The sum of double slice (X, Y, Z) is the total of A[X + 1] + A[X + 2] + ... + A[Y − 1] + A[Y + 1] + A[Y + 2] + ... + A[Z − 1].

For example, array A such that:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
contains the following example double slices:

double slice (0, 3, 6), sum is 2 + 6 + 4 + 5 = 17,
double slice (0, 3, 7), sum is 2 + 6 + 4 + 5 − 1 = 16,
double slice (3, 4, 5), sum is 0.
The goal is to find the maximal sum of any double slice.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximal sum of any double slice.

For example, given:

    A[0] = 3
    A[1] = 2
    A[2] = 6
    A[3] = -1
    A[4] = 4
    A[5] = 5
    A[6] = -1
    A[7] = 2
the function should return 17, because no double slice of array A has a sum of greater than 17.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [3..100,000];
each element of array A is an integer within the range [−10,000..10,000].
"""

def solution(A):
    Maxi=0 ### we have to do the max sum ending on every i belonging to a from left to right and from right to left
    ReverseMaxi=0
    ascending=[]
    descending=[]
    n=len(A)
    for i in range(1,n-1):
        Maxi=max(Maxi+A[i],0)
        ascending.append(Maxi)
        ReverseMaxi=max(ReverseMaxi+A[n-1-i],0)
        descending.append(ReverseMaxi)
    descending.reverse()
    ### fix the extremes to have the option of not adding anything
    ascending=[0]+ascending
    descending=descending+[0]
    #### now we calculate the sums not counting i
    result=0
    for i in range(n-2):
        result=max(result,ascending[i]+descending[i+1])
    print(ascending, descending, result)    
    return(result)
    pass

B=[3,2,6,-1,4,5,-1,2]
A=[5, 17, 0, 3]
solution(B)

