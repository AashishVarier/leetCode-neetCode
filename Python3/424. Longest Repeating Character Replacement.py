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

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for l in range(len(s)):
            count, maxFreq = {}, 0
            for r in range(l,len(s)):
                count[s[r]] = 1 + count.get(s[r], 0)
                maxFreq = max(maxFreq,count[s[r]] )
                if (r - l + 1 - maxFreq ) <= k:
                    res = max(res, r - l + 1 )
        
        return res
        #T: O(n^2) n: length of string
        #S: O(m) m: uniqe char in string

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0 
        charSet = set(s)

        for c in charSet:
            count = l = 0
            for r in range(len(s)):
                if c == s[r]:
                    count +=1
                
                while (((r - l + 1) - count) > k):
                    if c == s[l]:
                        count -= 1
                    l +=1
                
                res = max(res, (r - l + 1))
        
        return res
    
    #T: O(mn) n: length of string, m: uniqe char in string
        #S: O(m) 