class Solution:
    def isHappy(self, n: int) -> bool:
        
        def getSquare(num:int):
            res = 0
            while num:
                d = num % 10
                res += d ** 2
                num = num // 10
            return res
        
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = getSquare(n)
        return n == 1
        
