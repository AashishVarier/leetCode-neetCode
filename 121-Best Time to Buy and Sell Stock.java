//121. Best Time to Buy and Sell Stock

class Solution {
    public int maxProfit(int[] prices) {
        
    int buy = Integer.MAX_VALUE ,sell = 0, left = 0 , right = 0;
        
    while (right != prices.length){
        if(prices[left] < buy){
            buy = prices[left];
            
        } else if(prices[left] > prices[right]){
            buy = prices[right];
            left = right;
        }
        
        
        if(sell <= (prices[right] - buy)){
            sell = prices[right] - buy;
        }
        right ++; 
    }   
     
        return sell;
    }
}