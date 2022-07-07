# Question Link 
# https://leetcode.com/problems/relative-sort-array/


class Solution:
    # O(max(n,m)) Time O(1) Space
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_map = {}
        
        for i in range(len(arr2)) :
            hash_map[arr2[i]] = i
        
        # Bucket Sort
        length = len(arr2)
        buckets = [[]for i in range(1001 + length)]
        
        for num in arr1 :
            if num in hash_map :
                buckets[hash_map[num]].append(num)
            else:
                buckets[length+num].append(num)

        
        return [num for bucket in buckets for num in bucket]
       