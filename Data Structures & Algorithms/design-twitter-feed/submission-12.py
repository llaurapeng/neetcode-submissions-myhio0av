import heapq
from typing import List

class Twitter:

    def __init__(self):
        self.count = 0  # This will act as a timestamp (we decrement it to get most recent tweet)
        self.map = {}  # Dictionary to store user data: userId -> [tweets, followers]

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1  # Decrement count to ensure most recent tweets have smaller values

        if userId not in self.map:
            self.map[userId] = [[], []]  # Initialize with an empty list of tweets and followees

        self.map[userId][0].append([self.count, tweetId])  # Add the new tweet

    def getNewsFeed(self, userId: int) -> List[int]:
        curr = []
 
        curr.extend(self.map[userId][0])

        # Add tweets from all users they follow
        following = self.map[userId][1] # Get the list of followees (second part of the list)
        for followeeId in following:
            if followeeId in self.map:
                curr.extend(self.map[followeeId][0])  # Add their tweets

        # Convert to max-heap by negating the timestamp (count)
      
        heapq.heapify(curr)  # Heapify the list

        ret = []
        # Retrieve the 10 most recent tweets
        for i in range(10):
            if curr:
                count, tweetId = heapq.heappop(curr)  # Pop the most recent tweet (smallest negative count)
                ret.append(tweetId)
            else:
                break

        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return  # A user cannot follow themselves

        if followerId not in self.map:
            self.map[followerId] = [[], []]  # Initialize if the follower doesn't exist
        
        # Add the followee to the list of followees (to follow)
        if followeeId not in self.map[followerId][1]:
            self.map[followerId][1].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return  # A user cannot unfollow themselves

        if followerId not in self.map:
            return  # The follower doesn't exist

        if followeeId in self.map[followerId][1]:
            self.map[followerId][1].remove(followeeId)  # Remove followee from the list of followers



        
