# t = O(n^2)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        i,j = 0,0
        answer = [1]* len(nums)
        print(answer)
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    answer[i] = answer[i] * nums[j]
            
        
        return answer

