class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        available = [[time[0], time [1], dex] for dex, time in enumerate (tasks)]
        heapq.heapify (available)
        pending = []
        heapq.heapify (pending)
        time = 0
        ret = []
        

        while available or pending: 

            if not pending and available: 
                time = max (time, available [0][0])
        
            '''
            Put all available processes into pending
            '''
            while available and available [0][0] <= time: 
                #get rid of lowest enque time
                enqueTime, processTime, dex = heapq.heappop (available)
                #add to pending
                heapq.heappush (pending, [processTime, enqueTime, dex])

            if pending:
                processTime, enqueTime, dex = heapq.heappop (pending)
                ret.append (dex)
                time+= processTime
        return ret





            

            




        

