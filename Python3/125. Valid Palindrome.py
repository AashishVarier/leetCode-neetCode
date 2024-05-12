##neetCode soln
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not self.alphanum(s[l]):
                l += 1
            while l < r and not self.alphanum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

    # Could write own alpha-numeric function
    def alphanum(self, c):
        return (
            ord("A") <= ord(c) <= ord("Z")
            or ord("a") <= ord(c) <= ord("z")
            or ord("0") <= ord(c) <= ord("9")
        )


#using inbuilt function
    class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        new = ""
        if s == "":
            return True
        
        for i in s:
            if i.isalnum():
                new += i.lower()

        return new == new[::-1]  

##NOTE
#- output: true if palindrome, else false
#- input: String S
#- constraints: not null, printable ASCII char, ignore case, only alphanum
#-Soln:
	#- 2 ptr
		#	- T:O(n^2), S: O(1)
		#	- drawback: 
			
					
					
	#- Data Structure: reversal 
		#	-T:O(n) , S: O(n)
		#	- drawback: 
		
