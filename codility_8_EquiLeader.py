# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 21:19:22 2022

@author: Elkin Gutierrez
"""
"""
A non-empty array A consisting of N integers is given.

The leader of this array is the value that occurs in more than half of the elements of A.

An equi leader is an index S such that 0 ≤ S < N − 1 and two sequences A[0], A[1], ..., A[S] and A[S + 1], A[S + 2], ..., A[N − 1] have leaders of the same value.

For example, given array A such that:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
we can find two equi leaders:

0, because sequences: (4) and (3, 4, 4, 4, 2) have the same leader, whose value is 4.
2, because sequences: (4, 3, 4) and (4, 4, 2) have the same leader, whose value is 4.
The goal is to count the number of equi leaders.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the number of equi leaders.

For example, given:

    A[0] = 4
    A[1] = 3
    A[2] = 4
    A[3] = 4
    A[4] = 4
    A[5] = 2
the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000,000..1,000,000,000].
"""


def solution(A):
    ##### discover the dominant number
    stack=[]
    for i in A:
        if len(stack)==0:
            stack.append(i)
        elif stack[-1]==i:
            stack.append(i)
        else:
            stack.pop()
        #print(stack)
    if len(stack)==0:
        return(0) #### if there is not dominant return 0
    n=len(A)
    dom=stack[-1] #####this is my candidant
    times=0 ##### we count the number of times it is repeated
    for i in A:
        if i==dom:
            times+=1
    #print(times)
    
    equi=0  #### now we are going to count the number of times i divides A into two vectors with dom as a dominant number
    conteo=0
    for i in range(n):
        if dom==A[i]:
            conteo+=1
        if conteo>(i+1)/2 and (times-conteo)>(n-i-1)/2:
            equi+=1
        #print(conteo,(i+1)/2, (times-conteo),(n-i-1)/2)
    return(equi)
    pass


A=[4,3,4,4,4,2]
solution(A)