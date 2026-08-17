class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        res = [0] * len(digits)
        for i in range(len(digits)-1, -1, -1):
            s = carry + digits[i]
            print(s)
            res[i] = s % 10
            print(res)
            carry = s // 10
        
        return res if not carry else [carry] + res
        
        if carry:
            return [carry] + res
        else:
            return res
            