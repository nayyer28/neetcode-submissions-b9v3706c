import heapq
class Twitter:

    def __init__(self):
        self.heap = [] # maxHeap -> (tweetId, user)
        self.follows = {}
        self.count = 0
        # if userId == user or user in follows[userId]: then add to list otherwise skip

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.heap, (self.count, (tweetId, userId))) # O(log N)
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        temp = []
        i = 0
        while i < 10 and len(self.heap) > 0:
            c, (tweet, user) = heapq.heappop(self.heap)
            if user == userId or userId in self.follows and user in self.follows[userId]:
                res.append(tweet)
                i += 1
            temp.append((c,(tweet,user)))
            
        for tup in temp: # O(10 *log N)
            heapq.heappush(self.heap, tup)
        return res
            

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follows:
            self.follows[followerId] = set()
        self.follows[followerId].add(followeeId) # O(1) + O(1)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in  self.follows and followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId) # O(1) + O(1)
        
        
