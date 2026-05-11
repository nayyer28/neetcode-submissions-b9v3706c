class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        hand.sort()
        hmap = {}

        for h in hand:
            if h not in hmap:
                hmap[h] = 0
            hmap[h] += 1
        
        groups = len(hand) // groupSize
        
        while groups > 0:
            i = 0
            added = 0
            curr = hand[i]
            while added < groupSize and i < len(hand):
                if curr in hmap and hmap[curr] > 0:
                    added += 1
                    hmap[curr] -= 1
                    if hmap[curr] == 0:
                        del hmap[curr]
                    curr += 1
                    i += 1
                elif added > 0:
                    return False
                else:
                    i += 1
                    curr = hand[i]
            groups -= 1
        return True
            
        
        
        # 1 2 3 3 4 5 6 7
        # 3 5 6 7