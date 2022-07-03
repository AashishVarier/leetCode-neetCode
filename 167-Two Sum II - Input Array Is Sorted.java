//167. Two Sum II - Input Array Is Sorted

//time:O(n) space:O(n)
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] result = new int[2];
        for(int i = 0; i < numbers.length; i++){
            if( map.containsKey(target - numbers[i])){
                result[0] = map.get(target - numbers[i]) + 1;
                result[1] = i + 1;
                return result;
            }
            
            map.put( numbers[i] , i );
            
        }
        
        return result;
        
    }
}


//time:O(n) space:O(1)
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int left = 0, right = numbers.length - 1; 
        int[] result = new int[2];
        for(int i = 0; i < numbers.length; i++){
            if(numbers[left] + numbers[right] == target){
                result[0] = left + 1;
                result[1] = right + 1;
                return result;
            }
            
            else if(numbers[left] + numbers[right] > target){
                right = right - 1;
            }
            
            else{
                left = left + 1;
            }
            
        }
        
        return result;
        
    }
}