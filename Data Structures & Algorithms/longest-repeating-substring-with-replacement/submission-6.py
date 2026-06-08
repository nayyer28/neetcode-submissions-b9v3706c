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

            if (right - left + 1) - maxF > k:
                while (right - left + 1) - maxF > k: 
                    count[s[left]] -= 1
                    left += 1
                right += 1
                # now you never evaluate mxl for shrunk windows
            else: 
                mxl = max(mxl, (right - left + 1)) # only update mxl when right moves
                right += 1
        return mxl
        
                
            
            