# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 16:10:27 2022

@author: Elkin Gutierrez
"""
"""
A non-empty array A consisting of N integers is given. The consecutive elements of array A represent consecutive cars on a road.

Array A contains only 0s and/or 1s:

0 represents a car traveling east,
1 represents a car traveling west.
The goal is to count passing cars. We say that a pair of cars (P, Q), where 0 ≤ P < Q < N, is passing when P is traveling to the east and Q is traveling to the west.

For example, consider array A such that:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
We have five pairs of passing cars: (0, 1), (0, 3), (0, 4), (2, 3), (2, 4).

Write a function:

def solution(A)

that, given a non-empty array A of N integers, returns the number of pairs of passing cars.

The function should return −1 if the number of pairs of passing cars exceeds 1,000,000,000.

For example, given:

  A[0] = 0
  A[1] = 1
  A[2] = 0
  A[3] = 1
  A[4] = 1
the function should return 5, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer that can have one of the following values: 0, 1.
"""

#### sum the number of zeros until every 1


def solution(A):
    n=len(A)
    prefix=[0]*n
    counter=0
    for i in range(n):
        if A[i]==0:
            prefix[i]=0
            counter+=1
            print(counter)
        if A[i]==1:
            prefix[i]=counter
            print(prefix)
    result=sum(prefix)
    if result>1000000000:
        return(-1)
    else:
        return(result)

A=[0,1,0,1,1]
solution(A)



####another solution without no cache usage


### same but keep the prefix sum directly into the sum

def solution(A):
    n=len(A)
    prefix=[0]*n
    counter=0
    result=0
    for i in range(n):
        if A[i]==0:
            counter+=1
            print(counter)
        if A[i]==1:
            result+=counter
            print(prefix)
    if result>1000000000:
        return(-1)
    else:
        return(result)
