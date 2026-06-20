class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # triplets = [[1,2,3],[4,1,1],[7,1,1], [8,1,1]], target = [7,2,3]
        # res = [1,2,3]
        def merge(t1: List[int], t2: List[int]):
            return [max(t1[0], t2[0]), max(t1[1], t2[1]), max(t1[2], t2[2])]
        
        def consider(t: List[int], tar: List[int]):
            if t[0] > tar[0] or t[1] > tar[1] or t[2] > tar[2]:
                return False
            else:
                return True
        
        res = [0,0,0]
        for t in triplets:
            if consider(t, target):
                res = merge(res, t)
        
        return res == target
            