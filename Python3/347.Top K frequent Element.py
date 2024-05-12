class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        res =[]

        for i in nums:
            countDict[i] = 1 + countDict.get(i, 0)
            
        pyListComprehension = [j for j in sorted(countDict, key = countDict.get, reverse = True)] #pyListComprehension returns type list , sorted(a, key with which to sort, boolean for reverse)
        for l in range(k):
            res.append(pyListComprehension[l])
        
        return res

#T: o(n  + nlogn)
            
            

       

        