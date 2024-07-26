class Solution:

    def encode(self, strs: List[str]) -> str:
        newStr = ""
        for i in strs:
            newStr =newStr+ str(len(i)) + '#' + str(i)
        return newStr


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j]!= '#':
                j +=1
            length = int(s[i:j])
            res.append(s[j+1: j+1 + length])
            i=j+1 + length
        return res

#T:O(n)