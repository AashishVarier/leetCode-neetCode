class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countDict = {}
        res =[]

        for i in nums:
            countDict[i] = 1 + countDict.get(i, 0)
            
        pyListComprehension = [j for j in sorted(countDict, key = countDict.get, reverse = True)] #pyListComprehension returns type list  ## By default, iterating over a dict iterates over its keys. ### sorted(a, key with which to sort, boolean for reverse) The key argument to sorted is a callable (e.g. a function) which takes one argument. https://stackoverflow.com/questions/39496096/understanding-dictionary-get-in-python -   that is,  it is 'countDict.get' here , so for each key in the dictionary, countDict.get(key) will be executed and the result of that will be used in comparison.
        for l in range(k):
            res.append(pyListComprehension[l])
        
        return res

#T: o(n  + nlogn)
            
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        countD = {}
        ans = []
        freqList = [[] for i in range(len(nums) + 1)]

        for i in range(len(nums)):
            countD[nums[i]]  = 1 + countD.get(nums[i] , 0)
        print(countD)
        for key,val in countD.items():
            freqList[val].append(key)
        print(freqList)

        for i in range(len(freqList) - 1 , 0 , -1):
            for j in freqList[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans

#T: O(n)

#not mine but can use heap
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            freq[num] = 1 + freq.get(num, 0)
        
        heap = []
        for num, freq in freq.items():
            heapq.heappush(heap, (freq,num)) #keep the smallest value at heap[0], elements sorted based on the first element on the tuple.
        
        most_freq = heapq.nlargest(k, heap) #find nlargest numbers T:O(nlog(t)) 
        
        result = [num for freq, num in most_freq]
        return result


        

       

        