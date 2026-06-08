class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        

        left = right = 0
        count = {}
        maxF = 0
        mxl = 0

        while right < len(s):
            char = s[right]
            count[char] = count.get(char,0) + 1

            maxF = max(maxF, count[char])

            # equation checks number of replacements you need in curr window
            # the maxF might be overestimated as we shrink window
            # point of while loop is only to move left and that is acheived even
            # with a stale maxF
            # mxl is not tarnished since in shrinking the length is never greater than whatever mxl has seen before
            # when right was only moving and mxl was increasing
            # more explicit consistent way would be to use an if-else-statement: See Solution 2
            while (right - left + 1) - maxF > k: 
                if s[left] in count:
                    count[s[left]] -= 1
                    if count[s[left]] == 0:
                        del count[s[left]]
                left += 1
            mxl = max(mxl, (right - left + 1))
            right += 1
        return mxl
        
                
            
            