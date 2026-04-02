
class Twitter:

    def __init__(self):
        self.values = {}
        self.count = 0  # Timestamp for each tweet

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count += 1  # Increase timestamp (acts as the time order of tweets)
        
        if userId not in self.values:
            self.values[userId] = [[], []]  # If user doesn't exist, create empty tweet list and following list
        
        # Append the tweet in the format [timestamp, tweetId]
        self.values[userId][0].append([self.count, tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:
        # Check if the user exists
        if userId not in self.values:
            return []

        feed = []  # List to store all relevant tweets

        # Add tweets from the user themselves
        feed.extend( self.values[userId][0])

        # Add tweets from all users that the current user follows
        for followingID in self.values[userId][1]:
            if followingID in self.values:
                feed.extend(self.values[followingID][0])

        feed = [[-1 * count,id] for count, id in feed]
        heapq.heapify (feed)
        ret = []
        print (feed)

        for x in range (10):
            if feed:
                count, id = heapq.heappop (feed)
                ret.append (id)
            else: 
                break

        return ret



    def follow(self, followerId: int, followeeId: int) -> None:
        # Prevent following oneself
        if followerId == followeeId:
            return
        
        # If the follower doesn't exist, create their data structure
        if followerId not in self.values:
            self.values[followerId] = [[], []]

        # Add the followee to the follower's following list
        if followeeId not in self.values[followerId][1]:
            self.values[followerId][1].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        # Prevent unfollowing oneself
        if followerId == followeeId:
            return

        # Only unfollow if the follower exists and is following the followee
        if followerId in self.values and followeeId in self.values[followerId][1]:
            self.values[followerId][1].remove(followeeId)

