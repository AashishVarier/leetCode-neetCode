//78. Subsets


class Solution {
    public List<List<Integer>> subsets(int[] nums) {
        
        List<List<Integer>> answer = new ArrayList<>();
        Arrays.sort(nums);
        backtrack(answer, new ArrayList<>(), nums, 0);
        return answer;
        
    }
    
    public void backtrack(List<List<Integer>> answer, List<Integer> tempList, int[] nums, int start){
      if(nums.length == start){
        answer.add(new ArrayList<>(tempList)); //In java, we will have to add like this otherwise it'll give null as it'll just have the reference instead of actual values.
      }
        else{
            
            tempList.add(nums[start]); //add the element and start the  recursive call ie take nums[start]
            backtrack(answer, tempList, nums, start + 1);
            //remove the element and do the backtracking call ie dont take nums[start]
            tempList.remove(tempList.size() - 1);
            backtrack(answer, tempList, nums, start + 1);
            
        }
    
        
    }
    
}

