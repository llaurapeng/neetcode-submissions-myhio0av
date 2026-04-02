class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        candidates.sort()
        def dfs (i, sum, values):

            if sum == target: 
                ret.append (values[:])
                return 

            if sum > target or i >= len (candidates):
                return 

            values.append (candidates [i])

            dfs (i+1, sum + candidates [i], values)
            #back track 

            while i+1 < len (candidates) and candidates [i] == candidates [i+1]:
                i+=1

            values.pop ()

            dfs (i+1, sum, values)

        dfs (0,0, [])

        return ret



            


