# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 21:34:54 2022

@author: Elkin Gutierrez
"""
"""
A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

S is empty;
S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
S has the form "VW" where V and W are properly nested strings.
For example, the string "{[()()]}" is properly nested but "([)()]" is not.

Write a function:

class Solution { public int solution(String S); }

that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [0..200,000];
string S is made only of the following characters: "(", "{", "[", "]", "}" and/or ")".
"""

### make a dictionary to translate endings to openings and compare new elements in the stack to pop. and detect the elements to push.
def solution(S):
    stack = []
    keys = {"]":"[", "}":"{", ")": "("}
    topush = ["[", "{", "("]
    N=len(S)
    for i in range(0,N):
        if S[i] in topush:
            stack.append(S[i])
        elif keys[S[i]]!=stack.pop():
            return(0)
    if len(stack)==0:
        return(1)
    else:
        return(0)
    pass