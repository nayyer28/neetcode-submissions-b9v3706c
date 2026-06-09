class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        

        count1 = {}

        for c in s1:
            count1[c] = count1.get(c,0) + 1
        
        l = r = 0

        have, need = 0, len(count1)
        count2 = {}
        while r < len(s2):

            char = s2[r]
           
            if char not in count1:
                r += 1
                l = r
                count2 = {}
                have = 0
                continue
            
            count2[char] = count2.get(char, 0) + 1

            if count2[char] > count1[char]:
                while count2[char] > count1[char]:
                    if count2[s2[l]] == count1[s2[l]]:
                        have -= 1
                    count2[s2[l]] -= 1
                    l += 1
                r += 1
                continue


            if count2[char] == count1[char]:
                have += 1

            
            if have == need:
                return True
            
            r += 1
            
        
        return False
            
            
            
