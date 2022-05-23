# Question Link
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/


class Solution:
    # O(n) O(n)
    def removeDuplicates(self, s: str) -> str:
        stack = ['$'] # Place Holder
        
        for char in s :
            if char == stack[-1] :
                stack.pop()
                
            else:
                stack.append(char)
        return "".join(stack[1::])