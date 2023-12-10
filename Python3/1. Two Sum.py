class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i,j = 0,1
        ans = []
        while(i < len(nums)):
            j = j + i
            while(j < len(nums)):
                    if(nums[i] + nums[j] == target):
                        ans.append(i)
                        ans.append(j)
                        return ans

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checkMap = {}
        for i,n in enumerate(nums):
            if((target - n) in checkMap):
                return [i,checkMap[target - n]]
            checkMap[n] = i


##NOTE
- output: indices of tow numbers
- input: array of integers
- constraints: ip has one soln, no repition, return answere in any order, atleast 2 num in array
-Soln:
	- 2 ptr
			- T:O(n^2), S:O(1)
			- drawback: T:O(n^2)
			- check: 
	- Data Structure : HasMap
			- T:O(n^2), S:O(1)
			- drawback: T:O(n^2)
			- check: 
