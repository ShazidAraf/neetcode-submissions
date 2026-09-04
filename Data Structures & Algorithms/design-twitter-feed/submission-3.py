class Twitter:

    def __init__(self):

        self.tweet_map = defaultdict(list)
        self.follow_map = defaultdict(set)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time,tweetId])
        self.time = self.time-1

        

    def getNewsFeed(self, userId: int) -> List[int]:

        res = []
        min_heap = []

        self.follow_map[userId].add(userId)
        
        for followeeId in self.follow_map[userId]:

            if followeeId in self.tweet_map and len(self.tweet_map[followeeId]) > 0:
                index = len(self.tweet_map[followeeId]) - 1
                time, tweetId = self.tweet_map[followeeId][index]
                min_heap.append([time, tweetId, followeeId, index - 1])


        heapq.heapify(min_heap)
        count = 0
        # print(min_heap)

        while count<10 and min_heap:

            time, tweetId, followeeId, index = heapq.heappop(min_heap)
            res.append(tweetId)

            if index >= 0:
                time, tweetId = self.tweet_map[followeeId][index]
                heapq.heappush(min_heap, [time, tweetId, followeeId, index - 1])

            count+=1

        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)