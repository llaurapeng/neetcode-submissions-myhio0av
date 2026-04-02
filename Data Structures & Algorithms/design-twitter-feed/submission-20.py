class Twitter:

    def __init__(self):
        #users[id] = [[timestamp, tweetid(0)],[who they follow(1)]] 
        self.users = {}
        self.time = 0


    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time+=1

        if userId not in self.users: 
            self.users [userId] = [[],[]]

        self.users [userId][0].append ([int (self.time * -1), tweetId])

    def getNewsFeed(self, userId: int) -> List[int]:

        #print ('here')
        feed = []
        feed.extend (self.users[userId][0])

        for follow in self.users[userId][1]:
            if follow: 
                feed.extend (self.users [follow][0])
        heapq.heapify (feed)
        ret = []

        for x in range (10): 
            #print ('loop')
            if feed: 
                time, idv = heapq.heappop (feed)
                ret.append (idv)
            else: 
                break

        #print ('after')
        return ret


        
    def follow(self, followerId: int, followeeId: int) -> None:

        if followerId == followeeId: 
            return 

        if followerId not in self.users: 
            self.users [followerId] = [[],[followeeId]]

        if followeeId not in self.users[followerId][1]:
            self.users[followerId][1].append (followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        if followeeId in self.users[followerId][1]:
            self.users[followerId][1].remove(followeeId)


        
