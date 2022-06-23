//242. Valid Anagram

class Solution {
    public boolean isAnagram(String s, String t) {
        
       
        int[] alphabetBucket = new int[26];
        
        if(s.length() != t.length())
            return false;
        
        for(int i = 0; i < s.length() ; i++)
        {
            alphabetBucket[s.charAt(i) - 'a']++;
            alphabetBucket[t.charAt(i) - 'a']--;
        }
        
        for(int i : alphabetBucket ) {
         if(i!= 0)
            return false;
        
        }

        return true;
    }
}