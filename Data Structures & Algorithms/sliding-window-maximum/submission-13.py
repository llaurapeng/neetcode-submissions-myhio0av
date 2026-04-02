class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque ()
        ret = []
        l = 0

        for ind, num in enumerate (nums):
            while q and num > nums [q[-1]]:
                q.pop()

            q.append (ind)

            if l > q [0]:
                q.popleft()

            if (ind+1) >=k:
                ret.append (nums [q[0]])
                l+=1

        return ret




          


            
