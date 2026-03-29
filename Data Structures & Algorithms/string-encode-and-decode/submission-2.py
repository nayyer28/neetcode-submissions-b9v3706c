class Solution:

    def encode(self, strs: List[str]) -> str:
        out = ""

        for s in strs:
            out =  out + str(len(s)) + "#" + s
        return out

    def decode(self, s: str) -> List[str]:
        out = []
        i = 0
        while i < len(s):
            # find next # for length
            l = ""
            while s[i] != '#':
                l += s[i]
                i += 1
            nxt = s[i+1:i+1+int(l)]
            out.append(nxt)
            i = i + int(l) + 1
        return out


        