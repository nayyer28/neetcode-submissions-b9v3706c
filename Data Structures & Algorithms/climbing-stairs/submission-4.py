class Solution:
    def climbStairs(self, n: int) -> int:
        sol_prev, sol_prev_prev = 1, 1 # starting at 0 and 1

        for _ in range(2, n + 1):
            sol_prev_prev, sol_prev = sol_prev, sol_prev + sol_prev_prev
        
        return sol_prev