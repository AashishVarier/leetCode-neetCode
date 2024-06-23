class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0 
        res = 0
        countD = {}

        for r in range(len(s)):
            countD[s[r]] = countD.get(s[r], 0) + 1
            if (r-l + 1) - max(countD.values()) > k:
                countD[s[l]] -=1
                l += 1
            res = max(res, r-l +1)
        return res
    
    #T: O(26*n) = O(n)
    #S: O(n)