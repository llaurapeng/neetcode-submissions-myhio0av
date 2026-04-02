class MedianFinder:

    def __init__(self):
        self.values = []
        

    def addNum(self, num: int) -> None:
        self.values.append (num)

    def findMedian(self) -> float:
        heapcopy = self.values [:]
        heapq.heapify (heapcopy)
        leng = len (heapcopy)

        if leng % 2 != 0:
            mid = (leng //2) +1
        else: 
            mid = (leng //2)

        heapq.heapify (heapcopy)

        for i in range (mid):
            val = heapq.heappop (heapcopy)

        if leng % 2 == 0:
            otherval = heapq.heappop (heapcopy)

            return (otherval + val)/2

        return val

        


        
        