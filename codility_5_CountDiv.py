# -*- coding: utf-8 -*-
"""
Created on Thu Sep 15 18:53:27 2022

@author: Elkin Gutierrez
"""
"""
Write a function:

def solution(A, B, K)

that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }

For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Write an efficient algorithm for the following assumptions:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
"""


### i didnt use prefix sumes. just number theory
def solution(A, B, K):
    if A<K and A%K!=0:
        B=B-K
    else:    
        residual=A%K
        B=B-A-residual
    result=B//K
    return(result+1)


A,B,K=[101, 123456789, 10000]
A,B,K=[6, 11, 2]

solution(A, B, K)