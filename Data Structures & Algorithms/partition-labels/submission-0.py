class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # s = "xyxxyzbzbbisl"
        # x -> 3, y -> 2, z -> 2, b -> 3, i -> 1, s -> 1, l -> 1
        # xyxxy, zbzbb, i, s , l


        count = {}

        for c in s:
            count[c] = count.get(c, 0) + 1
        
        l = r = 0
        res = []
        window= {}
        distinct = set()
        need = have = 0
        while r < len(s):
            char = s[r]
            if char not in window:
                window[char] = 1
                need += 1
            else:
                window[char] += 1

            if window[char] == count[char]:
                have += 1
            
            if have == need:
                res.append(r + 1 - l)
                l = r + 1
                window = {}
                have = need = 0
            r += 1
        return res

