class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        

        s = []
        ret = [0] * len (temperatures)
        for ind, temp in enumerate (temperatures): 
            while s and temp > s [-1][0]:
                tempp, dex = s.pop()
                ret[dex] =  ind-dex
            s.append ([temp, ind])
        return ret



