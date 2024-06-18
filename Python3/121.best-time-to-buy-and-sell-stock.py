#T: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        res = 0

        for i in prices:
            if i < lowest:
                lowest = i
            res = max(res, i - lowest)
        return res
    
class Solution: #2ptr
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        r = 1
        profit = 0

        while(r < len(s)):
            if prices[l] < prices[r]:
                profit = max(profit, (prices[r] - prices[l]))
            else:
                l = r
            
            r+=1
        
        return profit

#T: O(n^2)

class Solution: #2ptr
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0

        for i in range(len(prices)):
            for j in range(i, len(prices)):
                profit = max(profit, (prices[j] - prices[i]))

        return profit

       