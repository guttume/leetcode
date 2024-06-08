class Twitter:

    def __init__(self):
        self.tweets = []
        self.follows = collections.defaultdict(set)
        self.count = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1
        heapq.heappush(self.tweets, (self.count * -1, tweetId, userId))

    def getNewsFeed(self, userId: int) -> List[int]:
        tweets = []
        kept = []
        i = 0
        while i < 10 and self.tweets:
            count, tweetId, fid = heapq.heappop(self.tweets)
            if fid == userId or fid in self.follows[userId]:
                tweets.append(tweetId)
                i += 1
            kept.append((count, tweetId, fid))

        for count, t, i in kept:
            heapq.heappush(self.tweets, (count, t, i))

        return tweets

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)