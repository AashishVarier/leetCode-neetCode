#using HashMap.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checkMap = {}
        for s in strs:
            sortedStrs = str(sorted(s))
            if sortedStrs not in checkMap:
                checkMap[sortedStrs] = []
            
            
            checkMap[sortedStrs].append(s)
        
        return list(checkMap.values())
    

##NOTES:
- output: List[List[str] 
- input: List[str]
- constraints: List size, values of list range
- Soln:
	- Using Data Structure : sort+ HashMap
			- T: O(n* mlogm) {n = lens(strs), mlogm sort complexity of longest string m} , S: O(nm)
    