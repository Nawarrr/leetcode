// Question Link
// https://leetcode.com/problems/is-subsequence/

class Solution {
    public boolean isSubsequence(String s, String t) {
        int i = 0;
        int j = 0;
        if (s.length() == 0){
            return true;
        }
        
        while (j < s.length() && i < t.length()){
            if (t.charAt(i) == s.charAt(j)) {
                i+=1;
                j+=1;
                if(j == s.length()){
                    return true ;
}
            } else {
                i+=1;
            }
        }
        return false;
        
    }
}