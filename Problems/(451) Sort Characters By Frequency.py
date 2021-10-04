# Question Link
# https://leetcode.com/problems/sort-characters-by-frequency/

# Description
'''
Given a string s, sort it in decreasing order based on the frequency of the characters. The frequency of a character is the number of times it appears in the string.

Return the sorted string. If there are multiple answers, return any of them.
'''

class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        heap = [(-v,k) for k,v in counter.items()]
        heapq.heapify(heap)
        output = ''
        while heap:
            letter = heapq.heappop(heap)[1]
            while counter[letter]:
                output+=letter
                counter[letter] -=1
        return output