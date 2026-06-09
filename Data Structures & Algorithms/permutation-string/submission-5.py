class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        
        count1, count2 = [0] * 26, [0] * 26

        for i in range(len(s1)):
            count1[ord(s1[i]) - ord('a')] += 1
            count2[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        
        for i in range(26):
            matches += (1 if count1[i] == count2[i] else 0)
        
        l = 0
        r = len(s1)

        while r < len(s2):
            if matches == 26:
                return True
            
            index = ord(s2[r]) - ord('a')
            count2[index] += 1

            if count2[index] == count1[index]:
                matches += 1
            elif count2[index] - 1 == count1[index]: # just when goes from a to aa and not to aaa after (only count match decreasing once)
                matches -= 1
            
            r += 1
            
            index = ord(s2[l]) - ord('a')
            count2[index] -= 1

            if count2[index] == count1[index]:
                matches += 1
            elif count2[index] + 1 == count1[index]: # just when goes from aaa to aa and not to a after (only count match decreasing once)
                matches -= 1
            
            l += 1
        
        return matches == 26
