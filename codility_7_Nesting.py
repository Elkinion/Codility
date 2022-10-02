# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 20:48:27 2022

@author: Elkin Gutierrez
"""
"""
A string S consisting of N characters is called properly nested if:

S is empty;
S has the form "(U)" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, string "(()(())())" is properly nested but string "())" isn't.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if string S is properly nested and 0 otherwise.

For example, given S = "(()(())())", the function should return 1 and given S = "())", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..1,000,000];
string S is made only of the characters "(" and/or ")".
"""

def solution(S):
    n=len(S)
    stack=[]
    
    for i in range(n):
        if S[i]=='(': ## if it is an open allways append
            stack.append(S[i])
        else:
            if len(stack)==0: ### if it is not and there are not opens return 0
                return(0)
            elif stack[-1]=='(':
                stack.pop()
    if len(stack)==0: ### if there is nothing left at the end it is a good array
        return(1)
    else:
        return(0)
        