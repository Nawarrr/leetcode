# Question Link
# https://leetcode.com/problems/apply-discount-to-prices/


class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        lst = sentence.split()
        
        for i in range(len(lst)):
            if len(lst[i]) >= 2 and lst[i][0] == '$' and all(ell.isdigit() for ell in lst[i][1::]):
                discounted = float(lst[i][1::]) - (float(lst[i][1::])*discount*(10**-2))
                string = str("$%.2f" % (discounted))
                lst[i] = string
        
        return " ".join(lst)
                