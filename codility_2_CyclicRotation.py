# -*- coding: utf-8 -*-
"""
Created on Sun Sep 11 14:19:23 2022

@author: Elkin Gutierrez
"""

"""An array A consisting of N integers is given. Rotation of the array means that each element is shifted right by one index, and the last element of the array is moved to the first place. For example, the rotation of array A = [3, 8, 9, 7, 6] is [6, 3, 8, 9, 7] (elements are shifted right by one index and 6 is moved to the first place).
The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
Write a function:
def solution(A, K)
that, given an array A consisting of N integers and an integer K, returns the array A rotated K times."""


def solution(A, K):
    N=len(A) #Number of integers in the array
    if N==0:
        return([])
    K=K%N #If k is too big we divide to make the function more eficient
    if K==0: #if it is 0 we dont need to move anything
        return(A)
    else: #rotate
        A=A[N-K:N]+A[0:N-K] #N-K for the last K numbers of the array
        return(A)
    


A = [3, 8, 9, 7, 6]
K = 3


solution(A, K)
