//3. Longest Substring Without Repeating Characters

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int windowSize = 0, left = 0, right = 0;
        Set<Character> windowSet = new HashSet<>();
        
        while(right < s.length()){
            if(!windowSet.contains(s.charAt(right))){
               windowSet.add(s.charAt(right));
                right ++;
            }
            else{
                windowSet.remove(s.charAt(left));
                left ++;
            }
            
            windowSize = Math.max(windowSize, (right - left));
            
        }
        
        return windowSize;
    }
}