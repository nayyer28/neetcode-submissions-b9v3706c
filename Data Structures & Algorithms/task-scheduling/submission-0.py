import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["A","A","A","B","C"]
        # a -> 1, b -> 1, c -> 1
        # A , n = 1
        # B , n = 2
        # C, n  = 3
        # idle, n = 4
        # A , n = 5
        # idle , n = 6
        # idle , n = 7
        # idle , n = 8
        # A , n = 9
        hmap = {}
        heap = []
        for t in tasks:
            if t not in hmap:
                hmap[t] = 1
                heap.append((0,t))
            else:
                hmap[t] += 1
        
        heapq.heapify(heap)
        curr = 0
        while len(heap) > 0:
            prio, nxt = heap[0]

            if curr >= prio:
                heapq.heappop(heap) # remove it
                # check if we have more tasks of nxt kind
                hmap[nxt] -= 1 
                if hmap[nxt] == 0:
                    del hmap[nxt]
                else:
                    heapq.heappush(heap,(prio+n+1, nxt))
            curr += 1
        return curr