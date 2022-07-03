//49. Group Anagrams
//O(n*m) n= length of array of string(strs) ; m = average length of string in the array string (s.length()).
class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        
        List<List<String>> resultLOL = new ArrayList<>();
        HashMap<String, List<String>> inListMap = new HashMap<>();
        
        
        if(strs == null ){
            return resultLOL;
        }
        //check for each sting in the array strs
        for(String s : strs){
      
            char[] alphaFreqCount = new char[26];
            for(int i = 0; i < s.length() ; i ++){
                alphaFreqCount[s.charAt(i) - 'a']++;
            }
            
            String mapsKey = new String(alphaFreqCount);
            //mapsKey not in HashMap, add new key=mapsKey and value= empty list
            if(!inListMap.containsKey(mapsKey))
                inListMap.put(mapsKey, new ArrayList<>());
         //add s to hashmap
            inListMap.get(mapsKey).add(s);
            
        }
        //add all values of hasmap to list of list
        resultLOL.addAll(inListMap.values());
        return resultLOL;
        
    }
}