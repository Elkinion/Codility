^^^^^# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 12:15:23 2022

@author: Elkin Gutierrez
"""
"""
A positive integer D is a factor of a positive integer N if there exists an integer M such that N = D * M.

For example, 6 is a factor of 24, because M = 4 satisfies the above condition (24 = 6 * 4).

Write a function:

def solution(N)

that, given a positive integer N, returns the number of its factors.

For example, given N = 24, the function should return 8, because 24 has 8 factors, namely 1, 2, 3, 4, 6, 8, 12, 24. There are no other factors of 24.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..2,147,483,647].
"""

def solution(N):
    if N==1:
        return(1)
    A=int(N**(1/2))+1 ### we will check until the square root and that wall give us also the divisors that are higher because for every D exist an M
    DivisorCount=0
    for i in range(1,A):
        if N%i==0 and i**2!=N:
            DivisorCount+=2
        elif N%i==0 and i**2==N:
            DivisorCount+=1
        #print(N%i,N,i)
    return(DivisorCount)

solution(25)