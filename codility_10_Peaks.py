# -*- coding: utf-8 -*-
"""
Created on Fri Sep 23 22:38:31 2022

@author: Elkin Gutierrez
"""
"""
A non-empty array A consisting of N integers is given.

A peak is an array element which is larger than its neighbors. More precisely, it is an index P such that 0 < P < N − 1,  A[P − 1] < A[P] and A[P] > A[P + 1].

For example, the following array A:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
has exactly three peaks: 3, 5, 10.

We want to divide this array into blocks containing the same number of elements. More precisely, we want to choose a number K that will yield the following blocks:

A[0], A[1], ..., A[K − 1],
A[K], A[K + 1], ..., A[2K − 1],
...
A[N − K], A[N − K + 1], ..., A[N − 1].
What's more, every block should contain at least one peak. Notice that extreme elements of the blocks (for example A[K − 1] or A[K]) can also be peaks, but only if they have both neighbors (including one in an adjacent blocks).

The goal is to find the maximum number of blocks into which the array A can be divided.

Array A can be divided into blocks as follows:

one block (1, 2, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2). This block contains three peaks.
two blocks (1, 2, 3, 4, 3, 4) and (1, 2, 3, 4, 6, 2). Every block has a peak.
three blocks (1, 2, 3, 4), (3, 4, 1, 2), (3, 4, 6, 2). Every block has a peak. Notice in particular that the first block (1, 2, 3, 4) has a peak at A[3], because A[2] < A[3] > A[4], even though A[4] is in the adjacent block.
However, array A cannot be divided into four blocks, (1, 2, 3), (4, 3, 4), (1, 2, 3) and (4, 6, 2), because the (1, 2, 3) blocks do not contain a peak. Notice in particular that the (4, 3, 4) block contains two peaks: A[3] and A[5].

The maximum number of blocks that array A can be divided into is three.

Write a function:

def solution(A)

that, given a non-empty array A consisting of N integers, returns the maximum number of blocks into which A can be divided.

If A cannot be divided into some number of blocks, the function should return 0.

For example, given:

    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 3
    A[5] = 4
    A[6] = 1
    A[7] = 2
    A[8] = 3
    A[9] = 4
    A[10] = 6
    A[11] = 2
the function should return 3, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000].
"""

def solution(A):
    n=len(A)
    peaks=[False]*n ### we make an array to find all peaks and count them
    numpeaks=0
    for i in range(1, n-1):
        if A[i - 1] < A[i] and A[i] > A[i + 1]:
            peaks[i]=True
            numpeaks+=1
    if numpeaks==0: ## take away the edge case of 0
        return(0)
    Next=[False]*n ## we find the next peak for every possition on a new array
    Next[-1]=-1
    for i in range (n-2,-1,-1):
        if peaks[i]:
            Next[i]=i
        else:
            Next[i]=Next[i+1]
    divisors=[]  ## we check for divisors under the squareroot
    sqrt=int(n**(1/2))+1
    for i in range(1,sqrt):
        if n%i==0:
            divisors.append(i)
            divisors.append(n//i)
    result=0
    for i in divisors: ### for every divisor check of the blocks have different numbers on the next peak list
        pos=0
        while pos<=n:
            if pos+i==n:
                if Next[pos+i-1]!=Next[pos]:
                    result=max(result,n//i)
                break
            elif Next[pos]!=Next[pos+i]:
                print(pos,i,Next[pos],Next[pos+i])
                pos+=i
            elif Next[pos]==Next[pos+i]:
                break
    return(result)
            
    print(peaks,divisors,Next,result)
    
        
A=[1, 5, 3, 4, 3, 4, 1, 2, 3, 4, 6, 2]
A=[5]
solution(A)



