class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += f"{l}#{s}"
        return res

    def decode(self, s: str) -> List[str]:
        p = 0
        res = []
        while p < len(s):
            l = ""
            while s[p] != '#':
                l += s[p]
                p += 1
            curr = s[p+1:p+1+int(l)]
            res.append(curr)
            p += 1 + int(l)
        return res

