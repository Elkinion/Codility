# -*- coding: utf-8 -*-
"""
Created on Tue Sep 27 20:52:27 2022

@author: Elkin Gutierrez
"""
"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A prime D is called a prime divisor of a positive integer P if there exists a positive integer K such that D * K = P. For example, 2 and 5 are prime divisors of 20.

You are given two positive integers N and M. The goal is to check whether the sets of prime divisors of integers N and M are exactly the same.

For example, given:

N = 15 and M = 75, the prime divisors are the same: {3, 5};
N = 10 and M = 30, the prime divisors aren't the same: {2, 5} is not equal to {2, 3, 5};
N = 9 and M = 5, the prime divisors aren't the same: {3} is not equal to {5}.
Write a function:

def solution(A, B).

that, given two non-empty arrays A and B of Z integers, returns the number of positions K for which the prime divisors of A[K] and B[K] are exactly the same.

For example, given:

    A[0] = 15   B[0] = 75
    A[1] = 10   B[1] = 30
    A[2] = 3    B[2] = 5
the function should return 1, because only one pair (15, 75) has the same set of prime divisors.

Write an efficient algorithm for the following assumptions:

Z is an integer within the range [1..6,000];
each element of arrays A and B is an integer within the range [1..2,147,483,647].
"""
def gcd(A, B):
    if A%B==0:
        return(B)
    else:
        return(gcd(B, A%B))

def sameprimes(A, B):
    value=gcd(A,B)
    while gcd(A,value)!=1:
        A=A//gcd(A,value)

    while gcd(B,value)!=1:
        B=B//gcd(B,value)
    if A==1 and B==1:
        return(True)
    else:
        return(False)


def solution(A, B):
    result=0
    n=len(A)
    for i in range(n):
        if sameprimes(A[i], B[i]):
            result+=1
    return(result)

A=[15,10,3]
B=[75,30,5]


solution(A, B)
