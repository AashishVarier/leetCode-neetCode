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

# t = O(n^2) S:O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #1[1,2,3,4]1
        #[24,12,4,1]
        #[1,1,2,6]
        post = [1 for i in range(len(nums))]
        pre = [1 for i in range(len(nums))]

        for i in range(len(nums)):
            if i == len(nums):
                post[i] = 1
            n = i
            while n+1 < len(nums):
                post[i] *= nums[n+1]
                n += 1
        
        for j in range(len(nums) -1,0, -1):
            if j == 0:
                post[j] = 1
            m = j
            while m -1 > -1:
                post[j] *= nums[m-1]
                m-=1
        
        return post

# t = O(n) S= O(1) assuming res is not considered
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1,2,3,4]
        #[1,12,8,6]24
        res = [1 for i in range(len(nums))]
        

        for i in range(1, len(nums)):
            res[i] = res[i -1 ] * nums[i -1]
        
        post =1
        for i in range(len(nums )-1, -1, -1):
            res[i] *=post
            post *= nums[i]
        
        return res

# T: O(n) S:O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #[1, 2, 3, 4] 
        pre = [1] * len(nums) #[1,1,2,6]
        suf = [1] * len(nums) #[24,12,4,1]
        res =[] #[24,12,8,6]
        for i in range(len(nums)):
            if i == 0:
                pre[i] = 1
            else:
                pre[i] = pre[i -1] * nums[i-1]

        for j in range((len(nums) -1), -1, -1 ):
            if j == len(nums) -1:
                suf[j] = 1
            else:
                suf[j] = suf[j +1] * nums[j+1]

        print(suf)
        print(pre)
        for k in range(len(nums)):
            res.append(suf[k]*pre[k])
        
        return res
