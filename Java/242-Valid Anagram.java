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


//Using Hashmap for Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?

class Solution {
    public boolean isAnagram(String s, String t) {
        HashMap<Character,Integer> smap=new HashMap<>();

        if(s.length() != t.length() ){
            return false;}

        for(int i=0;i<t.length();i++){
            smap.put(s.charAt(i),smap.getOrDefault(s.charAt(i),0)+1);
            smap.put(t.charAt(i),smap.getOrDefault(t.charAt(i),0)-1);

        }

        for(char c:smap.keySet()){
            if(smap.get(c)!=0){
                return false;}
        }
        
        return true;
    }
}