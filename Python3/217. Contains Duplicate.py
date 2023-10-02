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

        