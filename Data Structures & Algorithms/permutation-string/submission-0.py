class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        
        counts1 = {}

        for c in s1:
            counts1[c] = counts1.get(c,0) + 1
        
        left, right = 0,0
        counts2 = {}
        print("counts1", counts1)
        while right < len(s2):
            counts2[s2[right]] = counts2.get(s2[right], 0) + 1
            if right - left + 1 == len(s1):
                print("counts2", counts2)
                match = True
                for char, count in counts1.items():
                    match = match & ( char in counts2 and count == counts2[char] )
                if match:
                    return True
                counts2[s2[left]] -= 1
                left += 1
            right += 1
        
        return False