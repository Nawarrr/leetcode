class Solution:
    # O(Logn) Time O(1) Space
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        i = 0
        j = len(letters)
        
        
        while i < j :
            mid = (j+i)//2
            
            if target < letters[mid]:
                j = mid
            else:
                i = mid+1
                
        return letters[i % len(letters)]
            