class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge (left, right):
            res = [] 
            l = 0 
            r = 0 

            while l < len (left) and r < len (right):
                if left [l] <= right [r]:
                    res.append (left [l])
                    l+=1

                elif right[r] < left [l]:
                    res.append (right[r])
                    r+=1

            if r < len (right):
                res.extend (right [r:])
            if l < len (left):
                res.extend (left [l:])
            return res

        def helper (vals):
            if len (vals) <= 1: 
                return vals
            mid = len (vals)//2
            left = helper (vals [:mid])
            right = helper (vals [mid:])

            return merge (left, right)

        return helper (nums)





            
        