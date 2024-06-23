class Solution:
    def minWindow(self, s: str, t: str) -> str:
        resLen = sys.maxsize
        res = [-1,-1]
        countTD={}
        windCountD ={}
        l = 0
        if t == "":
            return ""
        for i in t:
            countTD[i] = countTD.get(i, 0) + 1
        have, need = 0, len(countTD)
        for r in range(len(s)):
            char = s[r]
            windCountD[char] = windCountD.get(char, 0) + 1

            if char in countTD and countTD[char] == windCountD[char]:
                have +=1
            
            while have == need:
                if (r -l + 1) < resLen:
                    resLen = r -l + 1
                    res=[l, r]
                windCountD[s[l]] -= 1
                if s[l] in countTD and windCountD[s[l]] < countTD[s[l]]:
                    have -=1
                l+=1
            
        l,r = res

        return s[l:r+1] if resLen != sys.maxsize else  ""
        
#T: O(n)



        
            
            
            
