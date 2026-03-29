class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        def is_alphanumeric(k: str):
            if ord(k) >= ord("a") and ord(k) <= ord("z") or ord(k) >= ord("A") and ord(k) <= ord("Z") or ord(k) >= ord("0") and ord(k) <= ord("9"):
                return True
            return False

        while left < right:
            # move left to alphanumeric
            if not is_alphanumeric(s[left]):
                left += 1
                continue
            # move right to alphanumeric
            if not is_alphanumeric(s[right]):
                right -= 1
                continue
            if not s[left].lower() == s[right].lower():
                return False
            
            left += 1
            right -= 1
            
        return True
