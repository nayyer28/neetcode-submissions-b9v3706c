class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = prices[0]
        mx = 0
        for i in range(1, len(prices)):

            if prices[i] > lowest: # found a larger number
                mx = max(mx, prices[i] - lowest)
            elif prices[i] < lowest:
                lowest = prices[i]
        
        return mx 