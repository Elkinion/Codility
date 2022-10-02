# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 15:38:03 2022

@author: Elkin Gutierrez
"""
"""
An array A consisting of N integers is given. A triplet (P, Q, R) is triangular if 0 ≤ P < Q < R < N and:

A[P] + A[Q] > A[R],
A[Q] + A[R] > A[P],
A[R] + A[P] > A[Q].
For example, consider array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
Triplet (0, 2, 4) is triangular.

Write a function:

def solution(A)

that, given an array A consisting of N integers, returns 1 if there exists a triangular triplet for this array and returns 0 otherwise.

For example, given array A such that:

  A[0] = 10    A[1] = 2    A[2] = 5
  A[3] = 1     A[4] = 8    A[5] = 20
the function should return 1, as explained above. Given array A such that:

  A[0] = 10    A[1] = 50    A[2] = 5
  A[3] = 1
the function should return 0.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""
## for a sorted array A[i]+A[i-1]>A[i-2] and A[i]+A[i-2]>A[i-1] for all i because A[i] is already bigger than A[i-2] and A[i-1]. then we only
## need to find a triplet where A[i-2]+A[i-1]>A[i] whitch is the third condition and we only need to check consecutive positions.
def solution(A):
    A.sort()
    n=len(A)
    if n<3:
        return(0)
    for i in range(n-2):
        if A[i]+A[i+1]>A[i+2]:
            return(1)
    return(0)
    pass