##neetCode soln
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        return countS == countT

##soln using internal function
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        return sorted(s) ==  sorted(t)

##NOTE
#- output: True if anagram else False
#- input: two strings s & t
#- constraints: s & t lowercase English, not null
#-Soln:
#	- Data Structure: HashMap
#			- T:O(n) , S:O(s+t)
#			- drawback: S:O(s+t)

			
	
#	- sort string:
#			- T: O(nlogn) bubble sort, S: O(n) space for sort
#			- drawback : sorting

