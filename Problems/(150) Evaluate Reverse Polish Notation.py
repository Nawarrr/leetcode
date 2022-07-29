# Question Link
# https://leetcode.com/problems/evaluate-reverse-polish-notation/

class Solution:
    # O(n) Time and Space
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        expressions = ['+','-','*','/']
        for token in tokens :
            if token in expressions :
                second_op = s.pop()
                first_op = s.pop()
                s.append(str(int(eval(first_op + token + second_op))))
                
            else :
                s.append(token)
        return int(s.pop())