# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    # O(Logn) Time O(1) Space
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n 
        while True :
            mid = (r+l) //2
            curr_guess = guess(mid) 
            if not curr_guess : return mid
            elif curr_guess == 1 : l = mid+1
            else: r = mid
        
            