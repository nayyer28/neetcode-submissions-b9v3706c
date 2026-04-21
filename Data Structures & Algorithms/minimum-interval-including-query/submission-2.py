# min heap + sorting
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        res = [-1] * len(queries) # solution array
        imap = {} # hmap - O(q)

        for ix, query in enumerate(queries):
            if query not in imap:
                imap[query] = [False, []]
            imap[query][1].append(ix)

        intervals.sort(key=lambda x: x[0]) # O(i log i)
        queries.sort() # O(q log q)
        heap = []
        q = i = 0

        # O(q + i)
        while q < len(queries):
            if not imap[queries[q]][0]: # guard to not process same query again

                while i < len(intervals) and intervals[i][0] <= queries[q]:
                    heapq.heappush(heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1])) # O(log i)
                    i += 1
                
                while heap and heap[0][1] < queries[q]:
                    heapq.heappop(heap) # O(log i)
                
                if heap:
                    for ix in imap[queries[q]][1]: # O(q)
                        res[ix] = heap[0][0]
                    imap[queries[q]][0] = True
                
            q += 1
        # total time complexity => # O(i log i) + # O(q log q) + O(2 i log i) + O(q)
        # asymptotic time complexity is O(q log q + i log i)
        return res