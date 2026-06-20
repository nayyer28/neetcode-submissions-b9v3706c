class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        count = {}

        for h in hand:
            count[h] = count.get(h,0) + 1
        
        for h in hand:
            start = h
            while start - 1 in count:
                start -= 1
            
            if start not in count:
                continue
            
            for n in range(start, start + groupSize):
                if n in count:
                    count[n] -= 1
                    if count[n] == 0:
                        del count[n]
                else:
                    return False
        return True