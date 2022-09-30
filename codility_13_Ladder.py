# -*- coding: utf-8 -*-
"""
Created on Wed Sep 28 14:27:37 2022

@author: Elkin Gutierrez
"""
"""
You have to climb up a ladder. The ladder has exactly N rungs, numbered from 1 to N. With each step, you can ascend by one or two rungs. More precisely:

with your first step you can stand on rung 1 or 2,
if you are on rung K, you can move to rungs K + 1 or K + 2,
finally you have to stand on rung N.
Your task is to count the number of different ways of climbing to the top of the ladder.

For example, given N = 4, you have five different ways of climbing, ascending by:

1, 1, 1 and 1 rung,
1, 1 and 2 rungs,
1, 2 and 1 rung,
2, 1 and 1 rungs, and
2 and 2 rungs.
Given N = 5, you have eight different ways of climbing, ascending by:

1, 1, 1, 1 and 1 rung,
1, 1, 1 and 2 rungs,
1, 1, 2 and 1 rung,
1, 2, 1 and 1 rung,
1, 2 and 2 rungs,
2, 1, 1 and 1 rungs,
2, 1 and 2 rungs, and
2, 2 and 1 rung.
The number of different ways can be very large, so it is sufficient to return the result modulo 2P, for a given integer P.

Write a function:

def solution(A, B)

that, given two non-empty arrays A and B of L integers, returns an array consisting of L integers specifying the consecutive answers; position I should contain the number of different ways of climbing the ladder with A[I] rungs modulo 2B[I].

For example, given L = 5 and:

    A[0] = 4   B[0] = 3
    A[1] = 4   B[1] = 2
    A[2] = 5   B[2] = 4
    A[3] = 5   B[3] = 3
    A[4] = 1   B[4] = 1
the function should return the sequence [5, 1, 8, 0, 1], as explained above.

Write an efficient algorithm for the following assumptions:

L is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..L];
each element of array B is an integer within the range [1..30].
"""

def solution(A, B):
    ###calculate the fibs but mod B
    n=max(A)
    maxb=2**max(B)
    F={}
    F[0]=1
    F[1]=1
    for i in range(2,n+2):
        F[i]=(F[i-1]+F[i-2])%maxb
    
    m=len(A) 
    res=[0]*m
    potenc={}
    potenc[0]=1
    potenc[1]=1
    for i in range(2,n+2):
        potenc[i]=potenc[i-1]*2
        print(potenc)
    for i in range(m):
        print(F[A[i]],(potenc[B[i]+1]))
        res[i]=F[A[i]]%(potenc[B[i]+1])
    return(res)
    
A=[4, 4, 5, 5, 1]
B=[3, 2, 4, 3, 1]

solution(A, B)



##### broken into many functions to understandl, but not 100%
def fib(n):
    F=[0]*(n+2)
    F[0]=1
    F[1]=1
    for i in range(2,n+2):
        F[i]=F[i-1]+F[i-2]
    return(F)



def fibmodb(A, B):
    F=fib(A+1)
    res=F[A]%(B**2)
    return(res)
    pass


def solution(A,B):
    n=len(A) 
    result=[0]*n
    for i in range(n):
        result[i]=fibmodb(A[i],B[i])
    return(result)
