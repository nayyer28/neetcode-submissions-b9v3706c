class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {c:i for i, c  in enumerate(s)}

        l = r = 0
        res = []
        for i, c in enumerate(s):

            r = max(r, last[c])

            if i == r:
                res.append(r - l + 1)
                l = i + 1
        return res
