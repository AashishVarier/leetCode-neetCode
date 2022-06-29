//1. Two Sum

//Brute Force O(n^2)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        for(int i = 0; i < nums.length; i ++){
            for(int j = nums.length - 1; j > i; j --){
                if(target == (nums[i] + nums[j])){
                    ans[0] = i ;
                    ans[1] = j;
                    return ans;
                }
            }
        }
        return null;
        
    }
}


//HashMap O(n)
class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] ans = new int[2];
        HashMap<Integer, Integer> seen = new HashMap<>();
        for(int i = 0 ; i < nums.length; i++){
            if(seen.containsKey(target - nums[i])){
                ans[0] = seen.get(target - nums[i]);
                ans[1] = i;
                return ans;
                
            }
            seen.put(nums[i], i);
            
        }
     return ans;   
    }
}