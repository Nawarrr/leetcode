# Question Link
# https://leetcode.com/problems/partition-labels/


# Description
'''
You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

Return a list of integers representing the size of these parts.
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastApperance = {c:i for i, c in enumerate(s)}
        lastIndex = 0
        count = 0
        output = []
        for j in range(len(s)):
            lastIndex = max(lastIndex,lastApperance[s[j]] )
            count +=1
            if j == lastIndex:
                output.append(count)
                count =0
        return output