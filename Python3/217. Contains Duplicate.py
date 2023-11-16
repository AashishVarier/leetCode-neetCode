##T: O(n^2)  S: O(1)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if(nums[i] == nums[j]):
                    return True
        return False
        

##T: O(n) S: O(n)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        checkSet = set()
        for i in nums:
            if(i in checkSet):
                return True
            checkSet.add(i)
        
        return False

##NOTES:
- output: True if value repeats at least twice else False
- input: array / List
- constraints: List size, values of list range
- Soln:
	- Brute forece : two pointer 
			- T:O(n^2), S:O(1)
			- drawback: T:O(n^2)

	
	- Using Data Structure : Set
			- T: O(n), S: O(n)
			- drawback: S: O(n)
    
    - Using sorting
