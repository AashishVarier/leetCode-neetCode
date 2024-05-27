class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort() #sort O(nlogn) Tims Sorting algo take S: O(n)

        for i, v in enumerate(nums): #loop 1
            l,r = i+1 , len(nums)-1
            if i>0 and v == nums[i -1]:
                continue
                
            while l<r: #loop 2
                threeSum = v + nums[l] + nums[r]
                

                if threeSum > 0 :
                    r-=1
                elif threeSum < 0:
                    l+=1
                else:
                    ans.append([v, nums[l] , nums[r]])
                    l+=1
                    r-=1
                    while nums[l] == nums[l - 1] and l < r:  #loop 3
                        l += 1
        
        return ans
    
    #T: O(n^2) + O(nlogn) + O(n)= ((loop1*loop2)+ sort + loop3)=  O(n^2) 
    #(why loop3 is O(n) = https://stackoverflow.com/questions/60009657/big-o-complexity-of-three-nested-loops-with-the-last-loop-in-an-if-statement)
    #S: O(n)