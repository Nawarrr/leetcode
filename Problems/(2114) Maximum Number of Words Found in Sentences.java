// Question Link
// https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution {
    public int mostWordsFound(String[] sentences) {
        int gmx = 0;
        for (String sentence : sentences){
            String[] splitedS = sentence.split(" ");
            int lmx = 0;
            for (String s : splitedS){
                lmx+=1;
            }
            gmx = Math.max(gmx,lmx);
        }
        return gmx;
    }
}