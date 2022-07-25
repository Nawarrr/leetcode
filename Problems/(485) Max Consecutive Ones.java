// Question Link
// https://leetcode.com/problems/max-consecutive-ones/

class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max_so_far = 0 ;
        int count = 0;
        for(int num : nums){
            if (num == 1){
                count+=1;
                max_so_far = Math.max(max_so_far,count);
            } else {
                count = 0;
            }
        }
        return max_so_far ;
    }
}