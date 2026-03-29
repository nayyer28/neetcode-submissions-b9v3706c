class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)

        stack = []

        for i,t in enumerate(temperatures):

            if not stack:
                stack.append((t,i))
            
            else:
                while stack and t > stack[-1][0]:
                    pop_t, pop_i = stack.pop()
                    res[pop_i] = i - pop_i
                stack.append((t,i))
            
        return res
            
