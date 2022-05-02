class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Two Pass Soultion,  O(N) Time, O(N) Space  
        even = []
        odd = []
        for num in nums:
            if num % 2 ==0 :
                even.append(num)
            else:
                odd.append(num)
        
        return even+odd
        # O(N) Time, O(1) Space , Using Modified version of QuickSort
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums)-1
        while i < j:
            if nums[i] % 2 > nums[j] %2 :
                nums[i],nums[j] = nums[j] , nums[i]
            if nums[i] %2 == 0 :
                i+=1
            if nums[j]%2 == 1:
                j-=1
        return nums