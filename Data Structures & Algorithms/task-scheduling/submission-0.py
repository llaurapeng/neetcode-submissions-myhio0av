class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter (tasks)

        counter = list (counts.values())
        counter = [-1 * val for val in counter]
        heapq.heapify (counter)

        q = deque()
        time = 0

        while counter or q: 
            #counter has available times
            time+=1
            if counter:
            #if counter is not empty
                curr = heapq.heappop (counter)
                curr = curr + 1
                if curr != 0: 
                    q.append ([curr,time + n])

            else:
                #if counter is empty then nothing to process
                time = q[0][1]

            if q and time == q[0][1]:
                curr, time = q.popleft ()
                heapq.heappush (counter, curr)
            
        return time


                

        
        