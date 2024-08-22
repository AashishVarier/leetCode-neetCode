#using HashMap.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checkMap = {}
        for s in strs:
            sortedStrs = str(sorted(s)) #convert to str because of unhashable type: 'list'
            #sortedStrs = tuple(sorted(s)) #convert to tuple as tuple are immutable because of unhashable type: 'list'
            if sortedStrs not in checkMap:
                checkMap[sortedStrs] = []
            
            
            checkMap[sortedStrs].append(s)
        
        return list(checkMap.values()) #In Python 3, dict.values() (along with dict.keys() and dict.items()) returns a view, rather than a list
    

##NOTES:
#- output: List[List[str] 
#- input: List[str]
#- constraints: List size, values of list range
#- Soln:
	#- Using Data Structure : sort+ HashMap
			#- T: O(n* mlogm) {n = lens(strs), mlogm sort complexity of longest string m} , S: O(nm)
    #- Using Data Structure : array + HashMap
			#- T: O(n* m) {n = lens(strs), m length of longest string m} , S: O(nm)



class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checkMap = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] +=1           
            
            
            checkMap[tuple(count)].append(s)
        
        return list(checkMap.values())
    