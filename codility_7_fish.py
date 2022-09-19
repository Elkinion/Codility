# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 22:43:38 2022

@author: Elkin Gutierrez
"""


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


        