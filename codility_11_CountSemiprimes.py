# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 16:43:42 2022

@author: Elkin Gutierrez
"""
"""
A prime is a positive integer X that has exactly two distinct divisors: 1 and X. The first few prime integers are 2, 3, 5, 7, 11 and 13.

A semiprime is a natural number that is the product of two (not necessarily distinct) prime numbers. The first few semiprimes are 4, 6, 9, 10, 14, 15, 21, 22, 25, 26.

You are given two non-empty arrays P and Q, each consisting of M integers. These arrays represent queries about the number of semiprimes within specified ranges.

Query K requires you to find the number of semiprimes within the range (P[K], Q[K]), where 1 ≤ P[K] ≤ Q[K] ≤ N.

For example, consider an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
The number of semiprimes within each of these ranges is as follows:

(1, 26) is 10,
(4, 10) is 4,
(16, 20) is 0.
Write a function:

class Solution { public int[] solution(int N, int[] P, int[] Q); }

that, given an integer N and two non-empty arrays P and Q consisting of M integers, returns an array consisting of M elements specifying the consecutive answers to all the queries.

For example, given an integer N = 26 and arrays P, Q such that:

    P[0] = 1    Q[0] = 26
    P[1] = 4    Q[1] = 10
    P[2] = 16   Q[2] = 20
the function should return the values [10, 4, 0], as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..50,000];
M is an integer within the range [1..30,000];
each element of arrays P and Q is an integer within the range [1..N];
P[i] ≤ Q[i].
"""
### the usual sieve but with sqrt outside the loop and for loop.
def sieve(N):
    if N==1:
        return([False,False])
    sieve=[True]*(N+1)
    sieve[0]=sieve[1]=False
    i=2
    sqrt=int(N**(1/2))+1
    for i in range(2,sqrt+1):
        if sieve[i]:
            k=i*i
            while k<=N:
                sieve[k]=False
                k+=i
    return(sieve)    
    

def solution(N, P, Q):
    N=min(N,max(Q))
    sie=sieve(N)
    ###take the primes out of the sieve
    primes=[]
    for i in range(N+1):
        if sie[i]:
            primes+=[i]
    ###make a new sieve for the semiprimes
    semisieve=[0]*(N+1)
    for i in primes:
        for j in primes:
            if i*j>N:
                break
            else:
                semisieve[i*j]=1
        #primes.remove(i)
    count=0
    #### transform the sieve into a semicount list
    for i in range(N+1):
        if semisieve[i]==1:
            count+=1
        semisieve[i]=count
    M=len(P)
    result=[0]*M
    ### rest the results of the semicount for P and Q on each step
    for i in range(M):
        result[i]=semisieve[Q[i]]-semisieve[P[i]-1]
    return(result)
