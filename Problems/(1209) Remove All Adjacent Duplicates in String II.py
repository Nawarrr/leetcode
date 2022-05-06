# Question Link
# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/



class Solution:
    # O(n) Time , O(n) space
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [['#' , 0]] # Place Holder
        
        for char  in s :
            if stack[-1][0] == char:
                stack[-1][1]+=1
                if stack[-1][1] == k :
                    stack.pop(-1)
            else:
                stack.append([char,1])
        
        return "".join([char*count for char,count in stack[1::]])