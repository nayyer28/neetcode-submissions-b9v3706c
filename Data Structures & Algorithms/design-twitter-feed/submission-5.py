class Twitter:

    def __init__(self):
        self.count = 0
        self.follows = defaultdict(set) # default new keys get empty set
        self.tweets = defaultdict(list) # default new keys get empty list

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.count, tweetId))
        if len(self.tweets[userId]) > 10:
            self.tweets[userId].pop(0)
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        minHeap = []
        self.follows[userId].add(userId)
        if len(self.follows) >= 10: # later you process for most recent tweets. when you have more than 10 followees, you can already truncate your search set by ignoring the followee whose most recent tweet is the oldest in all the >10 followers.
            maxHeap = []
            for followeeId in self.follows[userId]:
                if followeeId in self.tweets:
                    index = len(self.tweets[followeeId]) - 1
                    count, tweetId = self.tweets[followeeId][index]
                    heapq.heappush(maxHeap, (-count, tweetId, followeeId,  index))
                    if len(maxHeap) > 10:
                        heapq.heappop(maxHeap)
            while maxHeap:
                count, followeeId, tweetId, index = heapq.heappop(maxHeap)
                heapq.heappush(minHeap, (-count, tweetId, followeeId,  index))
        else:
            for followeeId in self.follows[userId]:
                if followeeId in self.tweets:
                    index = len(self.tweets[followeeId]) - 1
                    count, tweetId = self.tweets[followeeId][index]
                    heapq.heappush(minHeap, (count, tweetId, followeeId,  index))
        while len(res) < 10 and minHeap:
            count, tweetId, followeeId,  index = heapq.heappop(minHeap)
            res.append(tweetId)
            index -= 1
            if index >= 0:
                count, tweetId = self.tweets[followeeId][index]
                heapq.heappush(minHeap, (count, tweetId, followeeId, index))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
