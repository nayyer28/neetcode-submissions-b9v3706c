class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # if prod is positive:
        # max_prod = prod since mag(int*int) is monotonically increasing
        # if prod is negative:
        # 1 * 2 * 3 * -4 * -8 * -100
        # if a neg int was seen before:
        # divide prod by last_greatest_neg
        # max_prod = max(max_prod, quotient)
        # else:
        # max_prod = max_prod
        # 2 4 -3 5
        # 2 8 -24          
        prod = 1    
        prefix = 1
        mx = float("-inf")
        for n in nums:
            prod = prod * n
            mx = max(mx, prod)
            if prod == 0:
                prod = 1
            elif prod < 0:
                mx = max(mx,prod // prefix)
                prefix = prod if prefix == 1 else max(prefix, prod)
            
        return mx