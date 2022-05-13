'''
Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''

class Solution:
    def isValid(self, s: str) -> bool:
        
        opening = ["(","{","["]
        closing = [")","}","]"]
        
        st = []
        
        for ch in s:
            
            if ch in opening:
                st.append(ch)
            
            elif ch in closing:
                pos = closing.index(ch)
                if len(st)>0 and opening[pos]==st[len(st)-1]:
                    st.pop()
                else:
                    return False
        
        return True if len(st)==0 else False
                
                