#T: O(n) S:O(n)

class Solution:
    def isValid(self, s: str) -> bool:
        checkD = {')': '(', '}':'{', ']': '['}
        stack = []

        for c in s:
            if c in checkD:
                if stack and stack[-1] == checkD[c]: #stack[-1] gives the last inserted element
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False

# Stack implemented using 
#1.list
#2.Collections.deque
#3.queue.LifoQueue