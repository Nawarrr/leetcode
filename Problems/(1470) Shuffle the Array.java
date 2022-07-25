// Question Link
// https://leetcode.com/problems/shuffle-the-array/


class Solution {
    public int[] shuffle(int[] nums, int n) {
        int i = 0;
        int j = n;
        int k = 0;
        int m = n*2;
        int [] output = new int[m];
        while(k < m){
            output[k] = nums[i];
            output[k+1] = nums[j];
            i+=1;
            j+=1;
            k+=2;
        }
        return output;

    }
}