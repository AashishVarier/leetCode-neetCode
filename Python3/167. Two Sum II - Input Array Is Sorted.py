#T : O(n)
#S: O(1)

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0 , len(numbers) -1
        while l< r:
            twoSum = numbers[l] + numbers[r]

            if twoSum == target:
                return [l+1,r+1]
            
            elif twoSum > target:
                r-=1
            else:
                l+=1

        