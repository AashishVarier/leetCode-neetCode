#T:O(n)

class Solution:

    def encode(self, strs: List[str]) -> str:
        eStr = ""
        for i in strs:
            eStr += str(len(i)) + "#" + i
        print (eStr)
        return eStr

    def decode(self, s: str) -> List[str]:
        dList = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j +=1    
            length = int(s[i:j])
            i = j + 1
            j = i + length
            dList.append(s[i:j])
            i=j
        return dList