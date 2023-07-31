//704. Binary Search

class Solution {
    public int search(int[] nums, int target) {
        
        int mid, left = 0, right = nums.length -1;
        
        while (left <= right){
            
            mid = left + (right - left)/2;
            
            if(target == nums[mid]){
                return mid;
            }    
            
            else if(target < nums[mid]) {
                right = mid -1;
            }
            
            else {
                left = mid + 1;
            }
                
        }
        
        return -1;
        
    }
}