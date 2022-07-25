// Question Link
// https://leetcode.com/problems/final-value-of-variable-after-performing-operations/

class Solution {
    public int finalValueAfterOperations(String[] operations) {
        int x = 0;
        for(String op : operations){
            if (op.contains("+")) {
                x+=1;
            } else {
                x-=1;
            }
            
        }
    return x;
    }
}