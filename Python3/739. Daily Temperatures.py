#T: O(n^2)
# S: O(n) for answer array

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = []
        for l in range(len(temperatures)):
            count = 1
            r = l + 1
            while r < len(temperatures):
                if temperatures[l] < temperatures[r]:
                    break
                r += 1
                count += 1
            count = 0 if r ==  len(temperatures) else count
            answer.append(count)
        
        return answer


#monotonic dexreasing stack soln
#t: O(n)
#S: O(n) for stack

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = [] # [[index, temp ]]

        for i, t in enumerate(temperatures):
            
            while stack and stack[-1][1] < t: #stack[-1][1] give temp at the top because stack = [[index, temp ]]
                stackI , stackT = stack.pop()
                answer[stackI] = (i - stackI)
            stack.append([i,t])
        
        return answer
