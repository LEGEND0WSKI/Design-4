# Time:
# Space:
# Leetcode: No
# Issues: want to create a maxheap for timestamp difference


import heapq
class Twitter:

    def __init__(self):
        self.followeesMap = {}  #{int , {int}} user: users
        self.tweetsMap = {}     #{int , [Tweet]} user: tweets
        self.timestamp = 0 
    
    class Tweet:
        def __init__(self, tweetId, timestamp):
            self.tweetId = tweetId
            self.createdAt = timestamp  

        def Twitter(self):
            self.followeesMap = {}
            self.tweetsMap = {}
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        self.follow(userId, userId)
        if userId in self.tweetsMap:
            self.tweetsMap[userId] = set()
        self.tweetsMap[userId].append(Twitter.Tweet(tweetId,self.timestamp))
    
    def getNewsFeed(self, userId: int) -> List[int]:
        pq = [] # a.createdat - b.createdAt // top 10
        
        followees = self.followeesMap[userId]
        if followees:
            for foll in followees:
                tweets = self.tweetsMap[foll]
                for tw in tweets:
                    heapq.heappush(pq,tw)
                    if len(pq) > 10:
                        heapq.heappop(pq)

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.followeesMap:
            self.followeesMap[followerId] = set()
        self.followeesMap[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.followeesMap and followerId != followeeId:
            self.followeesMap[followerId].discard(followeeId) # remove raises error


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)