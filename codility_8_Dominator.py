# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 19:23:17 2022

@author: Elkin Gutierrez
"""
"""
An array A consisting of N integers is given. The dominator of array A is the value that occurs in more than half of the elements of A.

For example, consider array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
The dominator of A is 3 because it occurs in 5 out of 8 elements of A (namely in those with indices 0, 2, 4, 6 and 7) and 5 is more than a half of 8.

Write a function

class Solution { public int solution(int[] A); }

that, given an array A consisting of N integers, returns index of any element of array A in which the dominator of A occurs. The function should return −1 if array A does not have a dominator.

For example, given array A such that

 A[0] = 3    A[1] = 4    A[2] =  3
 A[3] = 2    A[4] = 3    A[5] = -1
 A[6] = 3    A[7] = 3
the function may return 0, 2, 4, 6 or 7, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..100,000];
each element of array A is an integer within the range [−2,147,483,648..2,147,483,647].
"""

def solution(A):
    #### we get a candidat for dominant
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
        return(-1) ### if there is not even a cadidat at the end of the operation we return negative
    n=len(A)
    times=0   ### we count how many times it is repeated
    for i in A:
        if i==stack[-1]:
            times+=1
            
    if times>n/2:  ### now if it ocupies more than half of the vector we return one of the positions.
        return(A.index(stack[-1]))
    else:
        return(-1)
    pass

A=[3,4,3,2,3,-1,3,3]
A=[]
A=[2, 1, 1, 3, 4]
solution(A)