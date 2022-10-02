# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:43:38 2022

@author: Elkin Gutierrez
"""
"""
You are given two non-empty arrays A and B consisting of N integers. Arrays A and B represent N voracious fish in a river, ordered downstream along the flow of the river.

The fish are numbered from 0 to N − 1. If P and Q are two fish and P < Q, then fish P is initially upstream of fish Q. Initially, each fish has a unique position.

Fish number P is represented by A[P] and B[P]. Array A contains the sizes of the fish. All its elements are unique. Array B contains the directions of the fish. It contains only 0s and/or 1s, where:

0 represents a fish flowing upstream,
1 represents a fish flowing downstream.
If two fish move in opposite directions and there are no other (living) fish between them, they will eventually meet each other. Then only one fish can stay alive − the larger fish eats the smaller one. More precisely, we say that two fish P and Q meet each other when P < Q, B[P] = 1 and B[Q] = 0, and there are no living fish between them. After they meet:

If A[P] > A[Q] then P eats Q, and P will still be flowing downstream,
If A[Q] > A[P] then Q eats P, and Q will still be flowing upstream.
We assume that all the fish are flowing at the same speed. That is, fish moving in the same direction never meet. The goal is to calculate the number of fish that will stay alive.

For example, consider arrays A and B such that:

  A[0] = 4    B[0] = 0
  A[1] = 3    B[1] = 1
  A[2] = 2    B[2] = 0
  A[3] = 1    B[3] = 0
  A[4] = 5    B[4] = 0
Initially all the fish are alive and all except fish number 1 are moving upstream. Fish number 1 meets fish number 2 and eats it, then it meets fish number 3 and eats it too. Finally, it meets fish number 4 and is eaten by it. The remaining two fish, number 0 and 4, never meet and therefore stay alive.

Write a function:

class Solution { public int solution(int[] A, int[] B); }

that, given two non-empty arrays A and B consisting of N integers, returns the number of fish that will stay alive.

For example, given the arrays shown above, the function should return 2, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [0..1,000,000,000];
each element of array B is an integer that can have one of the following values: 0, 1;
the elements of A are all distinct.
Copyright 2009–2022 by Codility Limited. All Rights Reserved
"""

######## this is the working solution to 100%


### at the end of the eatings we are going to have an array of 0's followed by 1's. 
def solution(A,B):
    stack=[]
    n=len(A)
    alive=0
    for i in range(n):
        if B[i]==1: ## we will make an stack only with ones
            stack.append(A[i])
            alive+=1
        else:
            while len(stack)>0: ## if a zero comes we check the 1s stack and caclulate if it is empty we add the 0s
                if A[i]>stack[-1]:
                    stack.pop()
                    alive-=1
                else:
                    break
            if len(stack)==0:
                alive+=1
        print(stack) 
    return(alive)
    pass    


        

####### this is trying stacking 0s and 1s without result
def solution(A,B):
    stack=[]
    n=len(A)
    position=0
    for i in range(n):
        if B[i]==1:
            stack.append(A[i])
            position=i
        else:
            if len(stack)==0 or B[position]==0:
                stack.append(A[i])
                position=i
            elif B[position]==1 and A[i]<stack[-1]:
                next
            elif A[i]>stack.pop():
                stack.append(A[i])
                position=i
        print(stack)
    return(len(stack))
    pass



def solution(A,B):
    stack=[]
    n=len(A)
    position=0
    for i in range(n):
        if B[i]==1:
            stack.append(A[i])
            position=i
        elif len(stack)==0 or B[position]==0:
            stack.append(A[i])
            position=i
        while B[position]==1:
            if A[i]<stack[-1]:
                
            elif A[i]>stack.pop():
                position-=1
        
        print(stack)
    return(len(stack))
    pass




def solution(A,B):
    stack=[]
    direc=[]
    n=len(A)
    for i in range(n):
        if B[i]==1:
            stack.append(A[i])
            direc.append(B[i])
        elif len(stack)==0 or B[position]==0:
            stack.append(A[i])
            direc.append(B[i])
        while direc[-1]==1 and B[i]==0:
            if A[i]<stack[-1]:
                next
            elif A[i]>stack.pop():
                direc.pop()
        print(stack)
    return(len(stack))
    pass



def solution(A,B):
    stack=[]
    direc=[]
    n=len(A)
    for i in range(n):
        if B[i]==1:
            stack.append(A[i])
            direc.append(B[i])
        elif len(stack)==0 or direc[-1]==0:
            stack.append(A[i])
            direc.append(B[i])
        while direc[-1]==1 and B[i]==0:
            if A[i]<stack[-1]:
                #print(stack[-1],A[i])
                break
            elif A[i]>stack.pop():
                direc.pop()
                stack.append(A[i])
                direc.append(A[i])
        #print(stack[-1],A[i], B[i])
        #print(stack, direc)
    return(len(stack))
    pass

######## this is the working solution to 100%
def solution(A,B):
    stack=[]
    n=len(A)
    alive=0
    for i in range(n):
        if B[i]==1:
            stack.append(A[i])
            alive+=1
        else:
            while len(stack)>0:
                if A[i]>stack[-1]:
                    stack.pop()
                    alive-=1
                else:
                    break
            if len(stack)==0:
                alive+=1
        print(stack) 
    return(alive)
    pass    


        