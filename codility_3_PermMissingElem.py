# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 21:28:54 2022

@author: Elkin Gutierrez
"""

"""
An array A consisting of N different integers is given. The array contains integers in the range [1..(N + 1)], which means that exactly one element is missing.

Your goal is to find that missing element.

Write a function:

def solution(A)

that, given an array A, returns the value of the missing element.

For example, given array A such that:

  A[0] = 2
  A[1] = 3
  A[2] = 1
  A[3] = 5
the function should return 4, as it is the missing element.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
the elements of A are all distinct;
each element of array A is an integer within the range [1..(N + 1)].
"""


### with triangular number
def sol(A):
    n=len(A)
    suma=0
    for i in range(n):
        suma+=A[i]
    result=(n+1)*(n+2)//2-suma
    return(result)
    pass

### same logic with product
def solution(A):
    n=len(A)
    result=1
    prod=1
    for i in range(n):
        result*=A[i]
        prod*=(i+1)
    return(int(prod*(n+1)/result))
    pass



A= [2, 3, 1, 5]


sol(A)
