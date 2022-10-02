# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 16:13:40 2022

@author: Elkin Gutierrez
"""
"""
You are given an array A consisting of N integers.

For each number A[i] such that 0 ≤ i < N, we want to count the number of elements of the array that are not the divisors of A[i]. We say that these elements are non-divisors.

For example, consider integer N = 5 and array A such that:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
For the following elements:

A[0] = 3, the non-divisors are: 2, 6,
A[1] = 1, the non-divisors are: 3, 2, 3, 6,
A[2] = 2, the non-divisors are: 3, 3, 6,
A[3] = 3, the non-divisors are: 2, 6,
A[4] = 6, there aren't any non-divisors.
Write a function:

def solution(A)

that, given an array A consisting of N integers, returns a sequence of integers representing the amount of non-divisors.

Result array should be returned as an array of integers.

For example, given:

    A[0] = 3
    A[1] = 1
    A[2] = 2
    A[3] = 3
    A[4] = 6
the function should return [2, 4, 3, 2, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
each element of array A is an integer within the range [1..2 * N].
"""



def solution(A):
    n=len(A)
    result=[n]*n ### we will start with nobody divides everybody and then substract the ones dividing
    count={} ### we count the repetitions of every number on the array with a dictionary because we are going to access it several times latter and the hashing helps the speed
    for i in range(n):
        if A[i] in count:
            count[A[i]]+=1
        else:
            count[A[i]]=1
    previous={}
    for i in range(n):
        if (A[i]-1) in previous: ### if the number was evaluated before we take that answer and jump to the next, a little speed here
            result[i]=previous[A[i]-1]
            next
        else:
            sqrt=int(A[i]**(1/2)) 
            for j in range(1,sqrt+1): ### if it has not been evaluated before we substract the divisors with the number of repetitions from count 

                if A[i]%j==0:
                    if j**2==A[i]: ### if it is the exact square root then substrac one time
                        if j in count:
                            result[i]-=count[j]
                    else: ### if j*D=A[i] substract the repetitions from j and D
                        if j in count:
                            result[i]-=count[j]
                        if A[i]//j in count:
                            result[i]-=count[A[i]//j]
        previous[A[i]-1]=result[i] ### save the calculation in case the A[i] shows again latter
    return(result)
    pass

