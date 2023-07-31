//217. Contains Duplicate
class Solution {
    public boolean containsDuplicate(int[] nums) {
        
        HashSet<Integer> numbers = new HashSet<>();
        
        for(int n : nums){
            if(numbers.contains(n))
                return true;
            numbers.add(n);
        }
        
        return false;
        
   
    }
}