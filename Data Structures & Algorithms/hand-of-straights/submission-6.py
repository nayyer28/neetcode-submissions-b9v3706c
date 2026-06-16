import heapq
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        heapq.heapify(hand)

        while hand:
            i = 0
            curr = -1
            backfill = []
            while i < groupSize:
                nxt = heapq.heappop(hand)
                if curr == -1:
                    curr = nxt
                    i += 1
                    continue
                while nxt == curr and hand:
                    backfill.append(curr)
                    nxt = heapq.heappop(hand)
                if nxt != curr + 1:
                    return False
                curr = nxt
                i += 1
            for r in backfill:
                    heapq.heappush(hand, r)
        return True


        