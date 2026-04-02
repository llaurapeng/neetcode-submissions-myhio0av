class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        counts = Counter (tasks)

        heaper = list (counts.values())
        heaper = [-1 * val for val in heaper]
        heapq.heapify (heaper)

        q = deque()
        time = 0

        while heaper or q: 
            if heaper: 
                leftover = heapq.heappop(heaper)
                leftover = leftover + 1
                time+=1

                if leftover != 0: 
            
                    available = time + n 
                    q.append ([leftover, available])
            
            else: 
                time = q[0][1]

            if q and time == q[0][1]:
                leftover, available = q.popleft()
                heapq.heappush (heaper, leftover)

        return time

        
                

        
        