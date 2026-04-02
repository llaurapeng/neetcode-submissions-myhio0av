class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge (left, right):
            l,r = 0, 0
            ret = []

            while l < len (left) and r < len (right):
                if left [l] <= right [r]:
                    ret.append (left [l])
                    l+=1
                else: 
                    #if right is less than the left
                    ret.append (right [r])
                    r+=1
            if r <= len (right):
                ret.extend (right [r:])
            if l <= len (left):
                ret.extend (left [l:])
            return ret

        def helper (arr):
            if len (arr) == 1:
                return arr  

            mid = len (arr) // 2

            left = helper (arr [:mid])
            right = helper (arr [mid:])

            return merge (left, right)

        return helper (nums)





